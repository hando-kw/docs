from django.utils.translation import gettext as _

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from knox.models import AuthToken
from knox.settings import knox_settings
from knox.auth import TokenAuthentication
from knox.views import LogoutView as KnoxLogoutView

from app.users.models import User
from api.helpers.send_otp import OTPVerification
from api.helpers.utils import swagger_response
from api.helpers.mixins import SoftDeleteMixin
from .serializers import SendOtpSerializer, VerifyOtpSerializer, VerifyOtpResponseSerializer, UserProfileSerializer, UserAddressSerializer


class SendOtpView(APIView):
    serializer_class = SendOtpSerializer

    @swagger_response({
            200: {"detail": _("OTP sent successfully.")},
            400: {"mobile": [_("Invalid mobile number.")]},
            401: None,
            404: None,
        })
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        return OTPVerification.send_otp(mobile, "auth")

class VerifyOtpView(APIView):
    serializer_class = VerifyOtpSerializer

    def get_token_ttl(self):
        return knox_settings.TOKEN_TTL

    @swagger_response({
            200: VerifyOtpResponseSerializer,
            400 : {"detail": _("Invalid OTP.")},
            401: None,
            404: None,
        })
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        otp = serializer.validated_data["otp"]
        if OTPVerification.verify_otp(mobile, otp, "auth"):
            user, __ = User.objects.get_or_create(mobile=mobile)
            token_ttl = self.get_token_ttl()
            __, token = AuthToken.objects.create(user, token_ttl)
            return Response(
                VerifyOtpResponseSerializer({
                    "token": token,
                    "user": user
                    }).data,
                status=status.HTTP_200_OK,
            )
        return Response({"detail": _("Invalid OTP.")}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = None
    
    @swagger_response({
            200: None,
            204: {},
            400: None,
            404: None,
        })  
    def post(self, request, format=None):
        request._auth.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class ProfileRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = UserProfileSerializer
    http_method_names = ['get', 'patch']

    def get_object(self):
        return self.request.user
    
    @swagger_response({
            200: UserProfileSerializer,
            400: None,
            404: None,
        })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_response({
            200: UserProfileSerializer,
            400: None,
            404: None,
        })
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

class UpdateMobileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = SendOtpSerializer

    @swagger_response({
            200: {"detail": _("OTP sent successfully.")},
            400: {"mobile": [_("Invalid mobile number.")]},
            404: None,
        })
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        if request.user.mobile == mobile:
            return Response({"mobile": [_("Cannot update to the same mobile number.")],}, status=status.HTTP_400_BAD_REQUEST)
        
        if User.objects.filter(mobile=mobile).exists():
            return Response({"mobile": [_("User with this mobile number already exists.")],}, status=status.HTTP_400_BAD_REQUEST)
        
        return OTPVerification.send_otp(mobile, f'update-mobile-{request.user.id}')

class VerifyUpdateMobileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = VerifyOtpSerializer
    
    @swagger_response({
            200: {"detail": _("Mobile number update successfully.")},
            400: {"detail": _("Invalid OTP.")},
            404: None,
        })
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        mobile = serializer.validated_data["mobile"]
        otp = serializer.validated_data["otp"]
        if not OTPVerification.verify_otp(mobile, otp, f'update-mobile-{request.user.id}'):
            return Response({"detail": _("Invalid OTP.")}, status=status.HTTP_400_BAD_REQUEST)
        request.user.mobile = mobile
        request.user.save()
        request.user.auth_token_set.all().delete()
        return Response({"detail": _("Mobile number changed successfully.")}, status=status.HTTP_200_OK)

class UserAddressListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = UserAddressSerializer

    def get_queryset(self):
        return self.request.user.addresses.filter(is_deleted=False)

    @swagger_response({
            200: UserAddressSerializer,
            400: None,
            404: None,
        })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_response({
            200: UserAddressSerializer,
            400: {"address_type": [_("This field is required.")]},
            404: None,
        })
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

class UserAddressRetrieveUpdateDestroyView(SoftDeleteMixin, generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = UserAddressSerializer
    http_method_names = ['get', 'patch', 'delete']

    def get_queryset(self):
        return self.request.user.addresses.filter(is_deleted=False)

    @swagger_response({
            200: UserAddressSerializer,
            400: None,
        })
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    @swagger_response({
            200: UserAddressSerializer,
            400: {"address_type": [_("This field is required.")]},
            400: None,
        })
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)
    
    @swagger_response({
            200: None,
            204: {},
            400: None,
        })
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)