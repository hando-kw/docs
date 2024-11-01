from django.utils.translation import gettext_lazy as _

from rest_framework import serializers

from app.users.models import User, UserAddress
from api.helpers.utils import validate_mobile_number

class SendOtpSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)
    
    def validate_mobile(self, value):
        if not validate_mobile_number(value):
            raise serializers.ValidationError([_("Invalid mobile number.")])
        return value

class VerifyOtpSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=6)
    
    def validate_mobile(self, value):
        if not validate_mobile_number(value):
            raise serializers.ValidationError([_("Invalid mobile number.")])
        return value

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'fullname', 'email', 'mobile', 'date_joined']
        read_only_fields = ['id', 'mobile', 'date_joined']

class VerifyOtpResponseSerializer(serializers.Serializer):
    token = serializers.CharField()
    user = UserProfileSerializer()

class UserAddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = UserAddress
        exclude = ['is_deleted']