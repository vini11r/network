from rest_framework.viewsets import ModelViewSet

from element.models import Element, Product
from element.serializers import ElementSerializer, ProductSerializer


class ElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    serializer_class = ElementSerializer

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

