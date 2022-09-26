from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404


from .serializers import PacienteSerializer

from .models import Pacientes


class PacienteViewSet(ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Pacientes.objects.all()
    pagination_class = LimitOffsetPagination

    # def delete(self, request, id=None):
    #     paciente = get_object_or_404(Pacientes, id=id)
    #     paciente.delet()
    #     return Response({"status": "success", "data": "Item Deleted"})
