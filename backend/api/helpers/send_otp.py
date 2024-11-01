import pytz
from datetime import datetime, timedelta

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.crypto import get_random_string
from django.db.models import Q
from django.http import JsonResponse

from rest_framework import status
from rest_framework.response import Response

from app.users.models import UserOtp


class OTPVerification:
    OTP_LENGTH = getattr(settings, "OTP_LENGTH", 4)
    OTP_EXPIRATION_TIME = getattr(
        settings, "OTP_EXPIRATION_TIME", 60
    )  # Default: 1 minute
    UTC = pytz.UTC

    @staticmethod
    def generate_otp():
        return get_random_string(
            length=OTPVerification.OTP_LENGTH, allowed_chars="0123456789"
        )

    @staticmethod
    def send_otp(mobile: str, action: str = "reset-password") -> JsonResponse:
        """
        This method sends an OTP to the specified mobile number.

        Parameters:
        ----------
        mobile: str
            The mobile number to which the OTP will be sent.
        action: str
            The action for which the OTP will be sent.
            This is used to identify the OTP when verifying it.
            Default: 'reset-password'

        Returns:
        --------
        Response:
            A response object with the status of the OTP sending process.

        Example:
        --------
        >>> OTPVerification.send_otp('0123456789', 'reset-password')
        Response({'detail': 'OTP sent successfully.'}, status=200)
        """
        otp = OTPVerification.generate_otp()
        if UserOtp.objects.filter(
            mobile=mobile,
            action=action,
            expires_at__gte=OTPVerification.UTC.localize(datetime.now()),
        ).exists():
            return Response(
                {"detail": _("An OTP has already been sent to this mobile number.")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        UserOtp.objects.filter(
            (Q(mobile=mobile) & Q(action=action))
            | Q(expires_at__lt=OTPVerification.UTC.localize(datetime.now()))
        ).delete()
        try:
            # sms_gateway = SMS_SENDER()
            # is_sent = sms_gateway.send(
            #     mobile,
            #     f"Verification Code: {otp}",
            # )
            is_sent = True
            if not is_sent:
                return Response(
                    {"detail": _("Failed to send OTP.")},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR,
                )
            UserOtp.objects.create(
                mobile=mobile,
                otp=otp,
                action=action,
                expires_at=datetime.now()
                + timedelta(seconds=OTPVerification.OTP_EXPIRATION_TIME),
            )
            return Response(
                {"detail": _("OTP sent successfully.")}, status=status.HTTP_200_OK
            )
        except Exception as e:
            print(e)
            return Response(
                {"detail": _("Failed to send OTP.")},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
    
    @staticmethod
    def verify_otp(mobile: str, otp: str, action: str ='reset-password'):
        '''
        This method checks if the OTP is valid and deletes it.
        
        Parameters:
        ----------
        mobile: str
            The mobile number to which the OTP was sent.
        otp: str
            The OTP to be verified.
        action: str
            The action for which the OTP was sent.
            This is used to identify the OTP when verifying it.
            Default: 'reset-password'
        
        Returns:
        --------
        bool
            True if the OTP is valid, False otherwise.
            
        Example:
        --------
        >>> OTPVerification.verify_otp('0123456789', '123456', 'reset-password')
        True
        '''
        if not UserOtp.objects.filter(mobile=mobile, otp=otp, action=action, expires_at__gte=OTPVerification.UTC.localize(datetime.now())).exists():
            return False
        UserOtp.objects.filter((Q(mobile=mobile) & Q(action=action)) | Q(expires_at__lt=OTPVerification.UTC.localize(datetime.now()))).delete()
        return True
