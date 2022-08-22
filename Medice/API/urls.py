from django.urls import path
from .views import  User,Patient

urlpatterns = [
    path('usuario/', User.as_view()),
    path('paciente/', Patient.as_view()),
  
]