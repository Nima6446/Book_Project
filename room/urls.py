from django.urls import path
from room.views import rooms_list_page, RoomsListAPI
from . import views

urlpatterns = [
    path("list/", rooms_list_page, name="rooms_list"),
    path("api/v1/rooms/", RoomsListAPI.as_view(), name="api_rooms"),
]
