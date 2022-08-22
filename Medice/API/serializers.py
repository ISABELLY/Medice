import logging
from mailbox import NotEmptyError
from pyexpat import model
from rest_framework import serializers
from .models import Pacientes, Usuarios


#Criação do serializers de Usuarios
class usuario(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ('__all__')

 #Criação do serializers de Pacientes

class paciente(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fiels = ('__all__')
