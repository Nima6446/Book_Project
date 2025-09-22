from django.urls import path
from site_settings.views import SiteSettingsAPI, SliderListAPI

urlpatterns = [
    path("settings/", SiteSettingsAPI.as_view(), name="site-settings"),
    path("sliders/", SliderListAPI.as_view(), name="sliders-api"),

]
