from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

# 🟢 D'ABORD : OrderItemSerializer
class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity', 'price']
        read_only_fields = ['price']

# 🟡 PUIS : OrderWriteSerializer
class OrderWriteSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['order_items', 'status']

def create(self, validated_data):
    order_items_data = validated_data.pop('order_items', [])
    user = self.context['request'].user

    # 🔢 Calcule d'abord total_price
    total_price = 0
    for item_data in order_items_data:
        product = item_data['product']
        quantity = item_data['quantity']
        total_price += product.price * quantity

    # ✅ Crée la commande avec total_price déjà fourni
    order = Order.objects.create(
        user=user,
        status=validated_data.get('status', 'pending'),
        total_price=total_price
    )

    # 🧱 Crée ensuite les OrderItems avec les bons prix
    for item_data in order_items_data:
        product = item_data['product']
        quantity = item_data['quantity']
        item_price = product.price * quantity

        OrderItem.objects.create(
            order=order,
            product=product,
            quantity=quantity,
            price=item_price
        )

    return order


    def update(self, instance, validated_data):
        order_items_data = validated_data.pop('order_items', None)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if order_items_data is not None:
            instance.order_items.all().delete()
            total_price = 0
            for item_data in order_items_data:
                product = item_data['product']
                quantity = item_data['quantity']
                item_price = product.price * quantity
                total_price += item_price

                OrderItem.objects.create(
                    order=instance,
                    product=product,
                    quantity=quantity,
                    price=item_price
                )

            instance.total_price = total_price
            instance.save()

        return instance

# 🔵 ENFIN : OrderReadSerializer
class OrderReadSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_items', 'total_price', 'status', 'created_at', 'updated_at']
