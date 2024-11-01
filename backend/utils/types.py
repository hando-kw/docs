from django.utils.translation import gettext_lazy as _
from django.db import models

class AddressType(models.IntegerChoices):
    APARTMENT = 0, _("Apartment")
    HOME = 1, _("Home")
    OFFICE = 2, _("Office")

class OrderStatus(models.TextChoices):
    PENDING = 'pending', _('Pending')
    PROCESSING = 'processing', _('Processing')
    COMPLETED = 'completed', _('Completed')
    CANCELLED = 'cancelled', _('Cancelled')