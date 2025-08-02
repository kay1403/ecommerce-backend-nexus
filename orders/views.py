from rest_framework import viewsets, permissions
from .models import Order, OrderItem
from .serializers import OrderReadSerializer, OrderWriteSerializer, OrderItemSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return OrderReadSerializer
        return OrderWriteSerializer

    #def get_queryset(self):
       # user = self.request.user
       # if user.is_staff:
        #    return Order.objects.all()
       # return Order.objects.filter(user=user)
    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
          return Order.objects.none()
        user = self.request.user
        if not user.is_authenticated:
         return Order.objects.none()
        return Order.objects.filter(user=user)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        
        
    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def my_orders(self, request):
        orders = self.get_queryset().filter(user=request.user)
        serializer = self.get_serializer(orders, many=True)
        return Response(serializer.data)
    
class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
