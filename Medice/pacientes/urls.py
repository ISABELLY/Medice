from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PacienteViewSet

router = DefaultRouter()

router.register(r'', PacienteViewSet,basename="paciente")

# The API URLs are now determined automatically by the router.
urlpatterns = router.urls