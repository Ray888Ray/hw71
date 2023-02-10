from django.contrib.auth import get_user_model
from rest_framework import serializers
from webapp.models import Store, Order


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


class StoreSerializer(serializers.ModelSerializer):
    seller = AuthorSerializer(read_only=True)

    class Meta:
        model = Store
        fields = ['id', 'title', 'price', 'seller', 'created_at', 'orders', 'updated_at']
        read_only_fields = ['id', 'created_at', 'orders', 'updated_at']

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return Store.objects.create(**validated_data)


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'phone', 'address', 'store', 'customer', 'created_at', 'updated_at']
        read_only_fields = ['id', 'customer', 'created_at', 'updated_at']

    def validate(self, attrs):
        return super().validate(attrs)

    def create(self, validated_data):
        return Order.objects.create(**validated_data)