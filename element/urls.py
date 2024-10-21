from django.urls import path
from rest_framework.routers import DefaultRouter

from element.apps import ElementConfig
from element.views import ElementViewSet

app_name = ElementConfig.name

router = DefaultRouter()
router.register(r"element", ElementViewSet)

urlpatterns = [] + router.urls