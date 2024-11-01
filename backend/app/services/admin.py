from itertools import chain
from typing import Any

from django.http import HttpRequest
from django.utils.translation import gettext_lazy as _
from django.contrib import admin

from .models import MainCategory, SubCategory, Service

class ServiceInline(admin.StackedInline):
    model = Service
    extra = 0

class SubCategoryInline(admin.StackedInline):
    model = SubCategory
    extra = 0

@admin.register(MainCategory)
class MainCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ar', 'created_at', 'updated_at', 'is_deleted']
    fieldsets = (
        ('General', {
            'fields': ('name_en', 'name_ar', 'icon', 'is_deleted')
        }),
    )
    search_fields = ['name_en', 'name_ar']
    
    def get_inlines(self, request, obj) -> list:
        if not obj or (not obj.sub_categories.exists() and not obj.services.exists()):
            return [SubCategoryInline, ServiceInline]
        elif obj.sub_categories.exists():
            return [SubCategoryInline]
        else:
            return [ServiceInline]
    
    jazzmin_section_order = ['General', 'SubCategory', 'Service']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ar', 'parent', 'created_at', 'updated_at', 'is_deleted']
    search_fields = ['name_en', 'name_ar', 'parent__name_en', 'parent__name_ar']
    fields = ['name_en', 'name_ar', 'icon', 'parent', 'is_deleted']
    inlines = [ServiceInline]
    
    def get_form(self, request, obj=None, **kwargs):
        # Make parent field required and show only main categories in the dropdown
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['parent'].required = True
        form.base_fields['parent'].queryset = MainCategory.objects.all()
        return form

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name_en', 'name_ar', 'price', 'offer_price', 'category', 'created_at', 'updated_at', 'is_deleted']
    search_fields = ['name_en', 'name_ar', 'category__name_en', 'category__name_ar']
    list_filter = ['category']
    
    def get_form(self, request, obj=None, **kwargs):
        # Show available MainCategory and all SubCategory in the dropdown
        form = super().get_form(request, obj, **kwargs)
        sub_categories = SubCategory.objects.all()
        main_categories = MainCategory.objects.filter(sub_categories__isnull=True)
        combined_categories = list(chain(main_categories, sub_categories))
        choices = [(category.id, str(category)) for category in combined_categories]
        form.base_fields['category'].choices = choices
        return form
