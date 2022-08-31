from django.db import models

#Criação do models de Pacientes
class Pacientes(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30) 
    idade = models.IntegerField()
    data_nascimento = models.DateField()
    ativo = models.BooleanField(null=False, default=True)  
