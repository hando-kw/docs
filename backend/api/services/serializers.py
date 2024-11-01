from rest_framework import serializers

from app.services.models import Category, Service
from app.cart.models import Cart

from api.helpers.serializers import DynamicFieldsModelSerializer


class CartQuantitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'quantity']

class ServicesSerializer(DynamicFieldsModelSerializer):
    cart_details = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    discount_percentage = serializers.SerializerMethodField()
    has_offer = serializers.SerializerMethodField()
    service_includes_en = serializers.SerializerMethodField()
    service_includes_ar = serializers.SerializerMethodField()
    
    class Meta:
        model = Service
        exclude = ['updated_at', 'is_deleted']
    
    def get_cart_details(self, obj) -> CartQuantitySerializer:
        user_cart = getattr(obj, 'user_cart', None)
        if user_cart:
            return CartQuantitySerializer(user_cart[0]).data
        return None

    def get_duration(self, obj) -> int:
        if obj.id % 2 == 0:
            return 120
        return None
    
    def get_discount_percentage(self, obj) -> int:
        return obj.discount_percentage
    
    def get_has_offer(self, obj) -> bool:
        return obj.has_offer

    def get_service_includes_en(self, obj) -> list:
        if obj.id % 2 == 0:
            return ['Deep cleaning of the house', 'Washing the dishes', 'Ironing the clothes']
        return []
    
    def get_service_includes_ar(self, obj) -> list:
        if obj.id % 2 == 0:
            return ['تنظيف عميق للمنزل', 'غسيل الأطباق', 'تنظيف الملابس']
        return []

class CategorySerializer(DynamicFieldsModelSerializer):
    services = serializers.SerializerMethodField()
    class Meta:
        model = Category
        exclude = ['updated_at', 'is_deleted']
    
    def get_services(self, obj) -> ServicesSerializer:
        return ServicesSerializer(obj.services.all(), many=True, context=self.context).data

class ServicesCategoriesSerializer(CategorySerializer):
    sub_categories = serializers.SerializerMethodField()
    
    def get_sub_categories(self, obj) -> CategorySerializer:
        return CategorySerializer(obj.sub_categories.all(), many=True, context=self.context).data