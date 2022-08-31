from rest_framework import serializers
from .models import Pacientes


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'




# class paciente(serializers.ModelSerializer):
#     class Meta:
#         model = Pacientes
#         fields = '__all__'        