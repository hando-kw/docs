from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="cart", verbose_name=_("User"))
    service = models.ForeignKey("services.Service", on_delete=models.CASCADE, related_name="cart", verbose_name=_("Service"))
    
    quantity = models.PositiveIntegerField(validators=[MinValueValidator(1)], verbose_name=_("Quantity"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    class Meta:
        verbose_name = _("Cart")
        verbose_name_plural = _("Carts")
        constraints = [
            models.UniqueConstraint(fields=['user', 'service'], name='unique_cart', violation_error_message=_("This service is already in your cart."))
        ]