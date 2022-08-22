from email.errors import InvalidDateDefect
from mailbox import NotEmptyError
from django.db import models

#Criação do models de Usuarios
class Usuarios(models.Model):
    id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=200)
    senha = models.FloatField(max_length=30)
    nome = models.CharField(max_length=30)
    ativo = models.BooleanField(null=False, default=True)
