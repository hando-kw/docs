from rest_framework import serializers

from app.cart.models import Cart
from api.services.serializers import ServicesSerializer


class CartSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Cart
        fields = '__all__'
    
    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.save()
        return instance

class CartDetailSerializer(serializers.ModelSerializer):    
    service = ServicesSerializer()
    class Meta:
        model = Cart
        exclude = ['user',]

class CartResponseSerializer(serializers.Serializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    items = CartDetailSerializer(many=True)