from rest_framework import serializers

from app.lookups.models import City

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'