from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AgendaViewSet

router = DefaultRouter()

router.register(r'', AgendaViewSet,basename="Agenda")


urlpatterns = router.urls