from django.urls import path

urlpatterns = [
path("rooms-list/", RoomsLsit.as_view(), name="rooms_list"),
]
