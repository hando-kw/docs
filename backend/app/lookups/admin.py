from django.contrib import admin

from .models import City

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name_en', 'name_ar', 'created_at', 'updated_at')
    search_fields = ('name_en', 'name_ar')