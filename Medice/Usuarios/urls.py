from posixpath import basename
from webbrowser import get
from django.urls import path, include
from .views import  UsuarioViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('',UsuarioViewSet, basename="usuario")



urlpatterns = router.urls
