from django.urls import path
from . import views
from .views import index_page, IndexAPI

urlpatterns = [
    path("", index_page, name="home-page"),
    path("api/", IndexAPI.as_view(), name="home-api")
]