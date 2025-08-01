from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# ViewSet pour les catégories
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('id') 
    serializer_class = CategorySerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'slug']  # Permet la recherche par nom ou slug

# ViewSet pour les produits
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer

    # Ajout des fonctionnalités de filtrage, recherche et tri
    filter_backends = [
        DjangoFilterBackend,     # Pour les filtres exacts (ex: ?category=1)
        filters.OrderingFilter,  # Pour le tri (ex: ?ordering=price)
        filters.SearchFilter     # Pour la recherche (ex: ?search=chaussure)
    ]

    filterset_fields = ['category']  # Filtres exacts autorisés
    ordering_fields = ['price', 'name']  # Champs autorisés pour le tri
    search_fields = ['name', 'description']  # Champs recherchables
    permission_classes = [IsAuthenticatedOrReadOnly]
