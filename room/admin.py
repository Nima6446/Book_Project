from django.contrib import admin

from room.models import Property, Room, Availability

admin.site.register(Property)
admin.site.register(Room)
admin.site.register(Availability)
