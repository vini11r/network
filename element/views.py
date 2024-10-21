from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from element.models import Element, Product
from element.permissions import IsActive
from element.serializers import ElementSerializer, ProductSerializer


class ElementViewSet(ModelViewSet):
    queryset = Element.objects.all()
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    serializer_class = ElementSerializer
    search_fields = ("name", "country",)
    filterset_fields = ("country",)
    permission_classes = [IsActive]

    def perform_update(self, serializer):
        if "debt" in serializer.validated_data:
            serializer.validated_data.pop("debt")
            raise Exception("Вы не можете менять поле задолженности")
        super().perform_update(serializer)


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]

