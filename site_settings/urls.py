from django.urls import path
from site_settings.views import SiteSettingsAPI

urlpatterns = [
    path("settings/", SiteSettingsAPI.as_view(), name="site-settings"),
]
