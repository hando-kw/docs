from django.db import models
from django.utils.translation import gettext_lazy as _

class City(models.Model):
    name_en = models.CharField(max_length=256, verbose_name=_("Name (EN)"))
    name_ar = models.CharField(max_length=256, verbose_name=_("Name (AR)"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created At"))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Updated At"))

    def __str__(self):
        return f'{self.name_en} - {self.name_ar}'