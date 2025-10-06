from django.urls import path

from room.views import RoomsListAPI

urlpatterns = [
path("rooms-list/", RoomsListAPI.as_view(), name="rooms_list"),
]
