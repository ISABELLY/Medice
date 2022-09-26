from django.db import models



class Agenda(models.Model):
   id=models.AutoField(primary_key=True)
   paciente=models.ForeignKey('pacientes.Pacientes', on_delete=models.CASCADE)
   usuario=models.ForeignKey('Usuarios.Usuarios', on_delete=models.CASCADE)
   momento=models.DateField
   hora_inicio=models.TimeField
   hora_fim=models.TimeField
   obs=models.TextChoices
   created_at=models.DateTimeField(auto_now=True)
   arquivado=models.BooleanField( default=False)




