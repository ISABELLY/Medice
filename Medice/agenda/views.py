from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404


from .serializers import AgendaSerializers

from .models import Agenda


class AgendaViewSet(ModelViewSet):
    serializer_class = AgendaSerializers
    queryset = Agenda.objects.all()
    pagination_class = LimitOffsetPagination
