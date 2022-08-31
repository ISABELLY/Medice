from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination


from .serializers import PacienteSerializer

from .models import Pacientes


class PacienteViewSet(ModelViewSet):
    serializer_class = PacienteSerializer
    queryset = Pacientes.objects.all()
    pagination_class = LimitOffsetPagination