from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Count

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id')  # <-- Ajouté pour éviter le crash
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug']

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')  # <-- Ajouté ici aussi
    serializer_class = ProductSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.OrderingFilter,
        filters.SearchFilter
    ]

    filterset_fields = ['category']
    ordering_fields = ['price', 'name']
    search_fields = ['name', 'description']
permission_classes = [IsAuthenticatedOrReadOnly]

@action(detail=False, methods=['get'])
def popular(self, request):
    # Suppose que Product a une FK avec OrderItem
    products = Product.objects.annotate(order_count=Count('orderitem')).order_by('-order_count')[:10]
    serializer = self.get_serializer(products, many=True)
    return Response(serializer.data)

@action(detail=False, methods=['get'])
def low_stock(self, request):
    products = Product.objects.filter(stock__lte=5).order_by('stock')
    serializer = self.get_serializer(products, many=True)
    return Response(serializer.data)