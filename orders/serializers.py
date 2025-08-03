from rest_framework import serializers
from .models import Order, OrderItem
from products.models import Product
from django.contrib.auth import get_user_model

User = get_user_model()

class OrderItemWriteSerializer(serializers.ModelSerializer):
    product = serializers.PrimaryKeyRelatedField(queryset=Product.objects.all())

    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']  

class OrderItemReadSerializer(serializers.ModelSerializer):
    product = serializers.StringRelatedField()
    price = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']


class OrderReadSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    order_items = OrderItemReadSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'order_items', 'total_price', 'status', 'created_at', 'updated_at']


class OrderWriteSerializer(serializers.ModelSerializer):
    order_items = OrderItemWriteSerializer(many=True)

    class Meta:
        model = Order
        fields = ['order_items', 'status']  

    def create(self, validated_data):
        order_items_data = validated_data.pop('order_items')
        user = self.context['request'].user if 'request' in self.context else None

        
        order = Order.objects.create(user=user, status=validated_data.get('status', 'PENDING'), total_price=0)

        total = 0
        for item_data in order_items_data:
            product = item_data['product']
            quantity = item_data['quantity']
            price = product.price * quantity
            total += price
            OrderItem.objects.create(order=order, product=product, quantity=quantity, price=price)

        order.total_price = total
        order.save()
        return order


    def update(self, instance, validated_data):
        order_items_data = validated_data.pop('order_items', None)
        instance.status = validated_data.get('status', instance.status)
        instance.save()

        if order_items_data is not None:
            instance.order_items.all().delete()
            total = 0
            for item_data in order_items_data:
                product = item_data['product']
                quantity = item_data['quantity']
                price = product.price * quantity
                total += price
                OrderItem.objects.create(order=instance, product=product, quantity=quantity, price=price)

            instance.total_price = total
            instance.save()

        return instance
