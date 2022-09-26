from rest_framework import serializers

from .models import Agenda

class AgendaSerializers(serializers.ModelSerializer):

    class Meta:
        model=Agenda
        fields='__all__'

