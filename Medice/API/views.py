from ast import Return
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import usuario,paciente
from .models import Usuarios, Pacientes


#Criação do views de Usuarios 
class User(APIView):
    #def get (self,request):
    def post (self, request):
        serializers = usuario(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response ({"status": "success", "data": serializers.data}, status = status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializers.errors}, status = status.HTTP_400_BAD_REQUEST)


# Criação do views de Pacientes

class Patient(APIView):
    def post(self, request):
        serializers = paciente(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({"status": "success", "data": serializers.data}, status = status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializers.errors}, status = status.HTTP_400_BAD_REQUEST)



