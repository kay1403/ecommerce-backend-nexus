from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

# ----- Serializer des OrderItems -----
class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']
        #fields = ['url', 'order', 'product', 'quantity']



# ----- Serializer pour la lecture (GET) -----
class OrderReadSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_items', 'total_price', 'status', 'created_at', 'updated_at']


# ----- Serializer pour la création/mise à jour (POST/PUT) -----
class OrderWriteSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['order_items', 'total_price', 'status']

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items', [])
        user = self.context['request'].user if 'request' in self.context else None
        order = Order.objects.create(user=user, **validated_data)
        for item_data in order_items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        order_items_data = validated_data.pop('order_items', None)

        # Met à jour les champs de la commande
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if order_items_data is not None:
            # Supprimer tous les order_items précédents
            instance.order_items.all().delete()
            # Recréer les nouveaux order_items
            for item_data in order_items_data:
                OrderItem.objects.create(order=instance, **item_data)

        return instance
