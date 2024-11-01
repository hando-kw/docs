# talk about provider extra money structure

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, FileExtensionValidator
from decimal import Decimal

from utils.types import AddressType, OrderStatus
from utils.validators import FileSizeValidator
from app.users.models import User
from app.services.models import Service

# Add this new class for payment type choices
class PaymentType(models.TextChoices):
    CASH = 'cash', _('Cash')
    VISA = 'visa', _('Visa')
    APPLE_PAY = 'apple_pay', _('Apple Pay')

class OrderAddress(models.Model):
    name = models.CharField(max_length=256, verbose_name=_("Address Name"))
    building_name = models.CharField(max_length=256, verbose_name=_("Building Name"), null=True, blank=True)
    building_number = models.CharField(max_length=256, verbose_name=_("Building Number"), null=True, blank=True)
    street_name = models.CharField(max_length=256, verbose_name=_("Street Name"), null=True, blank=True)
    apartment_number = models.CharField(max_length=256, verbose_name=_("Apartment Number"), null=True, blank=True)
    floor_number = models.CharField(max_length=256, verbose_name=_("Floor Number"), null=True, blank=True)
    block_number = models.CharField(max_length=256, verbose_name=_("Block Number"), null=True, blank=True)
    additional_information = models.TextField(null=True, blank=True, verbose_name=_("Additional Information"))
    latitude = models.FloatField(verbose_name=_("Latitude"))
    longitude = models.FloatField(verbose_name=_("Longitude"))
    address_type = models.SmallIntegerField(choices=AddressType.choices, verbose_name=_("Address Type"), default=AddressType.HOME)
    city = models.CharField(max_length=256, verbose_name=_("City"), null=True, blank=True)

    class Meta:
        verbose_name = _("Order Address")
        verbose_name_plural = _("Order Addresses")

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name="orders", verbose_name=_("User"))
    address = models.ForeignKey(OrderAddress, on_delete=models.PROTECT, related_name="orders", verbose_name=_("Address"))
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Total Amount"), validators=[MinValueValidator(Decimal('0.00'))])
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING, verbose_name=_("Status"))
    note = models.TextField(blank=True, null=True, verbose_name=_("Note"))  # New field
    payment_type = models.CharField(max_length=20, choices=PaymentType.choices, default=PaymentType.CASH, verbose_name=_("Payment Type"))
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return f"Order {self.id} - {self.user.fullname}"

    @property
    def amount_paid(self):
        return sum(payment.amount for payment in self.payments.all())

    @property
    def outstanding_amount(self):
        return self.total_amount - self.amount_paid

    class Meta:
        verbose_name = _("Order")
        verbose_name_plural = _("Orders")

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", verbose_name=_("Order"))
    service = models.ForeignKey(Service, on_delete=models.PROTECT, related_name="order_items", verbose_name=_("Service"), null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name=_("Item Name"))
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name=_("Quantity"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"), validators=[MinValueValidator(Decimal('0.00'))])
    comment = models.TextField(blank=True, null=True, verbose_name=_("Comment"))

    
    def __str__(self):
        return f"{self.name} - {self.quantity}"


    class Meta:
        verbose_name = _("Order Item")
        verbose_name_plural = _("Order Items")

class OrderAttachment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="attachments", verbose_name=_("Order"))
    file = models.FileField(
        upload_to='order_attachments/',
        validators=[
            FileExtensionValidator(allowed_extensions=[
                'txt', 'pdf', 'doc', 'docx',
                'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'tif', 'webp', 'svg'
            ]),
            FileSizeValidator(max_size_mb=5)
        ],
        verbose_name=_("File")
    )
    file_name = models.CharField(max_length=255, verbose_name=_("File Name"))
    file_type = models.CharField(max_length=10, verbose_name=_("File Type"))
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Uploaded At"))

    def __str__(self):
        return f"Attachment for Order {self.order.id} - {self.file_name}"

    class Meta:
        verbose_name = _("Order Attachment")
        verbose_name_plural = _("Order Attachments")

class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="payments", verbose_name=_("Order"))
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Amount"), validators=[MinValueValidator(Decimal('0.01'))])
    payment_type = models.CharField(max_length=20, choices=PaymentType.choices, verbose_name=_("Payment Type"))
    transaction_id = models.CharField(max_length=255, blank=True, null=True, verbose_name=_("Transaction ID"))
    payment_date = models.DateTimeField(auto_now_add=True, verbose_name=_("Payment Date"))
    
    def __str__(self):
        return f"Payment of {self.amount} for Order {self.order.id}"

    class Meta:
        verbose_name = _("Payment")
        verbose_name_plural = _("Payments")