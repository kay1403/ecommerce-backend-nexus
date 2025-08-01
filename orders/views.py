from rest_framework import viewsets, permissions
from .models import Order, OrderItem
from .serializers import OrderReadSerializer, OrderWriteSerializer, OrderItemSerializer

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

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
