from django.urls import path
from .views import  User,Patient

urlpatterns = [
    path('Usuario/', User.as_view()),
    path('Paciente/', Patient.as_view()),
  
]