from django.urls import path
from .views import  User,Patient

urlpatterns = [
    path('usuario/', User.as_view()),
    path('paciente/', Patient.as_view()),
    path('usuario/<int:id>', User.as_view()),
    path('paciente/<int:id>', Patient.as_view()),

  ]