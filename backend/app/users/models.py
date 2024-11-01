from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_superuser(self, mobile, password, **extra_fields):
        user = self.model(
            mobile=mobile,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
    fullname = models.CharField(max_length=256, null=True, blank=True, verbose_name=_("Full Name"))
    email = models.EmailField(max_length=254, null=True, blank=True, verbose_name=_("Email"))
    mobile = models.CharField(max_length=15, unique=True, verbose_name=_("Mobile"))

    # unwanted fields
    username = None
    first_name = None
    last_name = None

    objects = UserManager()

    USERNAME_FIELD = "mobile"

    def clean(self):
        if self.email is not None:
            if User.objects.filter(email=self.email).exists():
                raise ValidationError({"email": _("User with this Email already exists")})
    
    def __str__(self):
        if self.username:
            return self.username
        else:
            return self.mobile


class UserOtp(models.Model):
    # fields
    mobile = models.CharField(max_length=15, verbose_name=_("Mobile"))
    otp = models.CharField(max_length=6, verbose_name=_("OTP"))
    action = models.CharField(max_length=128, verbose_name=_("Action"))
    expires_at = models.DateTimeField(verbose_name=_("Expires At"), )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))

    def __str__(self):
        return self.otp

ADDRESS_TYPE_CHOICES = (
    (0, _("Apartment")),
    (1, _("Home")),
    (2, _("Office")),
)

class UserAddress(models.Model):
    # fk fields
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="addresses", verbose_name=_("User"))
    city = models.ForeignKey("lookups.City", on_delete=models.PROTECT, related_name="addresses", verbose_name=_("City"), null=True, blank=True)
    # fields
    name = models.CharField(max_length=256, verbose_name=_("Name"))
    building_name = models.CharField(max_length=256, verbose_name=_("Building Name"), null=True, blank=True)
    building_number = models.CharField(max_length=256, verbose_name=_("Building Number"), null=True, blank=True)
    street_name = models.CharField(max_length=256, verbose_name=_("Street Name"), null=True, blank=True)
    apartment_number = models.CharField(max_length=256, verbose_name=_("Apartment Number"), null=True, blank=True)
    floor_number = models.CharField(max_length=256, verbose_name=_("Floor Number"), null=True, blank=True)
    block_number = models.CharField(max_length=256, verbose_name=_("Block Number"), null=True, blank=True)
    additional_information = models.TextField(null=True, blank=True, verbose_name=_("Additional Information"))
    latitude = models.FloatField(verbose_name=_("Latitude"))
    longitude = models.FloatField(verbose_name=_("Longitude"))
    address_type = models.SmallIntegerField(choices=ADDRESS_TYPE_CHOICES, verbose_name=_("Address Type"), default=1)
    is_deleted = models.BooleanField(default=False, verbose_name=_("Is Deleted"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return f'{self.user} - {self.name}'
