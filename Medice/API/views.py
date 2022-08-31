from ast import Return
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from .serializers import usuario, UserSerializer
from .models import Usuarios, Pacientes


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = Usuarios.objects.all()

#Criação do views de Usuarios 
class User(APIView):
 def post (self,request):
    #  def post (self, request):
        serializers = usuario(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response ({"status": "success", "data": serializers.data}, status = status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializers.errors}, status = status.HTTP_400_BAD_REQUEST)
# Implementando o metodo GET
# def get (self,request, id=None):
#         if id:
#             cadastro = Usuarios.objects.get(id=id)
#             serializers = usuario(cadastro)
#             return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)

#         cadastro = Usuarios.objects.all()
#         serializers = usuario(cadastro, many=True)
#         return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)

# Criação do views de Pacientes

class Patient(APIView):
    def get(self, request):
        serializer = paciente(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


#Implementação do metodo GET de pacientes 
#class Patien(APIView):
    # def get (self,request, id=None):
    #     if id:
    #         registro = Pacientes.objects.get(id=id)
    #         serializers = paciente(registro)
    #         return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)

    #     registro = Usuarios.objects.all()
    #     serializers = usuario(registro, many=True)
    #     return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)
            