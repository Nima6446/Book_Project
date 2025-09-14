from rest_framework import serializers
from .models import SiteSettings, Slider


class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = [
            "id",
            "site_name",
            "site_url",
            "site_logo",
            "addres",
            "tell",
            "email",
            "copy_right_text",
            "about_us_page",
            "is_main_settings",
        ]


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = [
            "id",
            "title",
            "url",
            "url_title",
            "descriptuon",
            "image",
            "is_active",
        ]
