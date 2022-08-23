from email.errors import InvalidDateDefect
from mailbox import NotEmptyError
from django.db import models

#Criação do models de Usuarios
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=200, null=False)
    senha = models.FloatField(max_length=30, null=False)
    nome = models.CharField(max_length=30)
    ativo = models.BooleanField(null=False, default=True)

#Criação do models de Pacientes
class Pacientes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30) 
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    ativo = models.BooleanField(null=False, default=True)  
