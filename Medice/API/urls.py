from django.urls import path
from .views import  User

urlpatterns = [
    path('Usuario/', User.as_view()),
  
]