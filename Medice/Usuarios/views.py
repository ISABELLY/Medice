from ast import Return
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination

from .serializers import UsuarioSerializer

from .models import Usuarios


class UsuarioViewSet(ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuarios.objects.all()
    pagination_class = LimitOffsetPagination


# #Criação do views de Usuarios 
# class User(APIView):
#  def post (self,request):
#     #  def post (self, request):
#         serializers = usuario(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response ({"status": "success", "data": serializers.data}, status = status.HTTP_200_OK)
#         else:
#             return Response({"status": "error", "data": serializers.errors}, status = status.HTTP_400_BAD_REQUEST)
# # Implementando o metodo GET
# def get (self,request, id=None):
#         if id:
#             cadastro = Usuarios.objects.get(id=id)
#             serializers = usuario(cadastro)
#             return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)

#         cadastro = Usuarios.objects.all()
#         serializers = usuario(cadastro, many=True)
#         return Response({"status": "success", "data": serializers.data}, status=status.HTTP_200_OK)


