from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, pagination

import room
from .models import Room
from .serializers import RoomSerializer



def rooms_list_page(request):
    return render(request, "rooms_list.html")

class RoomsListAPI(APIView):
    def get(self, request):
        rooms = Room.objects.filter(is_active=True).order_by(-Room.price)
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class RoomsPagination(pagination.PageNumberPagination):
    page_size = 9
