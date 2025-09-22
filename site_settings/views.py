from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import SiteSettings, Slider
from .serializers import SiteSettingsSerializer, SliderSerializer


class SiteSettingsAPI(APIView):
    def get(self, request):
        # گرفتن تنظیمات اصلی سایت
        settings = SiteSettings.objects.filter(is_main_settings=True).first()
        settings_data = None
        if settings:
            settings_data = SiteSettingsSerializer(settings).data
        return Response(
            {
                "settings": settings_data,
            },
            status=status.HTTP_200_OK
        )


class SliderListAPI(APIView):
    def get(self, request):
        sliders = Slider.objects.filter(is_active=True)
        serializer = SliderSerializer(sliders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
