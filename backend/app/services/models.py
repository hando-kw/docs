from decimal import Decimal

from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, FileExtensionValidator
from django.db import models
# import magic

# Create your models here.

# category -> product 
# category -> subcategory -> product

class Category(models.Model):
    name_en = models.CharField(max_length=256, verbose_name=_("Name (EN)"))
    name_ar = models.CharField(max_length=256, verbose_name=_("Name (AR)"))
    icon = models.FileField(upload_to="categories/icons/", null=True, blank=True, verbose_name=_("Icon"))
    parent = models.ForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, related_name="sub_categories", verbose_name=_("Main Category"))
    is_deleted = models.BooleanField(default=False, verbose_name=_("Is Deleted"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def clean(self) -> None:
        if self.parent == self:
            raise ValidationError(_("Category can't be parent of itself"))
        if self.parent and self.parent.parent:
            raise ValidationError(_("Category can't be sub category of sub category"))
        if self.parent and self.parent.services.count() > 0:
            raise ValidationError(_("Category can't have services"))
        super().clean()
    def __str__(self):
        return self.name_en if not self.parent else f"{self.name_en} - {self.parent.name_en}"
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

class MainCategory(Category):
    class Meta:
        proxy = True
        verbose_name = _("Main Category")
        verbose_name_plural = _("Main Categories")
    
    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(parent__isnull=True)
    
    objects = Manager()

class SubCategory(Category):
    class Meta:
        proxy = True
        verbose_name = _("Sub Category")
        verbose_name_plural = _("Sub Categories")
        
    
    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(parent__isnull=False)
    
    objects = Manager()

# def validate_svg(file):
#     # Check if the file is empty
#     if not file:
#         return
#     # Check the file type
#     file_type = magic.from_buffer(file.read(1024), mime=True)
#     if file_type != 'image/svg+xml':
#         raise ValidationError('File is not SVG.')

class Service(models.Model):
    # fk fields
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name=_("Category"), related_name="services")
    # fields
    name_en = models.CharField(max_length=256, verbose_name=_("Name (EN)"))
    name_ar = models.CharField(max_length=256, verbose_name=_("Name (AR)"))
    description_en = models.TextField(verbose_name=_("Description (EN)"))
    description_ar = models.TextField(verbose_name=_("Description (AR)"))
    tag_en = models.CharField(max_length=256, verbose_name=_("Tag (EN)"), null=True, blank=True)
    tag_ar = models.CharField(max_length=256, verbose_name=_("Tag (AR)"), null=True, blank=True)
    warranty = models.IntegerField(verbose_name=_("Warranty"), help_text=_("In months"), null=True, blank=True, validators=[MinValueValidator(0)])
    show_warranty = models.BooleanField(default=False, verbose_name=_("Show Warranty"))
    icon = models.FileField(
        upload_to="services/icons/",
        null=True,
        blank=True,
        verbose_name=_("Icon"),
        validators=[FileExtensionValidator(allowed_extensions=['svg'])],
        help_text=_("Upload SVG file only"),
    )
    image = models.ImageField(upload_to="services/images/", null=True, blank=True, verbose_name=_("Image"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price") ,validators=[MinValueValidator(Decimal(0.00))])
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, verbose_name=_("Offer Price"), validators=[MinValueValidator(Decimal(0.00))])
    is_deleted = models.BooleanField(default=False, verbose_name=_("Is Deleted"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))
    
    @property
    def has_offer(self):
        return self.offer_price is not None and self.offer_price > 0
    
    @property
    def discount_percentage(self):
        if self.offer_price and self.price:
            return round((self.price - self.offer_price) / self.price * 100, 2)
        return 0
    
    @property
    def discount_amount(self):
        if self.offer_price and self.price:
            return self.price - self.offer_price
        return 0
    
    @property
    def final_price(self):
        if self.has_offer:
            return self.offer_price
        return self.price

    def clean(self) -> None:
        if self.offer_price and self.offer_price >= self.price:
            raise ValidationError({"offer_price": _("Offer price should be less than price")})
        
        if self.category_id and self.category.parent is None and self.category.sub_categories.count() > 0:
            raise ValidationError({"category": _("Main category have sub categories")})
        
        super().clean()
        
    def __str__(self):
        return self.name_en
    
    class Meta:
        verbose_name = _("Service")
        verbose_name_plural = _("Services")
