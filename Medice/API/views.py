from turtle import home
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import usuario
from .models import Usuarios


#Criação do views de Usuarios 
class User(APIView):
    def get (self,request):

    def post (self, request):
        serializer = usuario(data = request.data)
        if serializer.is_valid():
            return Response ({"status": "success", "data": serializer.data}, status = status.HTTP_200_OK)
        else:
                return Response({"status": "error", "data": serializer.errors}, status = status.HTTP_400_BAD_REQUEST)

