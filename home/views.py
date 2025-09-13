from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

def index_page(request):
    return render(request, "home/index.html")

class IndexAPI(APIView):
    def get(self, request):
        data = {
            "title": "سلام نیما",
            "desc": "به پروژه DRF خوش اومدی!"
        }
        return Response(data)

