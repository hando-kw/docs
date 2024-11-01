from django.conf import settings
from django.utils.translation import get_language

from rest_framework import serializers

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def to_representation(self, instance):
        result = super().to_representation(instance)
        lang = get_language()
        all_supported_languages = list(dict(settings.LANGUAGES).keys())
        for field_name in self.fields.keys():
            if field_name.endswith(f"_{lang}"):
                original_field_name = field_name.replace(f"_{lang}", "")
                # drop all other languages
                for language in all_supported_languages:
                    if language != lang:
                        result.pop(f"{original_field_name}_{language}", None)
                result[original_field_name] = result.pop(field_name)
        return result
