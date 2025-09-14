from django.contrib import admin

import site_settings
from site_settings.models import Slider, SiteSettings

admin.site.register(SiteSettings)
admin.site.register(Slider)
