from rest_framework.viewsets import ModelViewSet

from element.models import Element
from element.serializers import ElementSerializer


class ElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

