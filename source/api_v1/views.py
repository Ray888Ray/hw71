from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from webapp.models import Store, Order
from api_v1.serializers import StoreSerializer, OrderSerializer


class StoreViewSet(ModelViewSet):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return super().get_permissions()

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(seller=self.request.user)


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAdminUser]

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        else:
            return [IsAdminUser()]
        # return super().get_permissions()

    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(customer=self.request.user)