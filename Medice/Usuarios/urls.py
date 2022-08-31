from posixpath import basename
from webbrowser import get
from django.urls import path, include
from .views import  UsuarioViewSet

from rest_framework.routers import DefaultRouter

router = DefaultRouter()


router.register('',UsuarioViewSet, basename="usuario")


# The API URLs are now determined automatically by the router.
urlpatterns = router.urls

# urlpatterns = [
#     path('usuario/', UsuarioViewSet.as_view(get)),
#   ]