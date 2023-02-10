from django.urls import path, include
from api_v1.views import StoreViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

app_name = 'api_v1'

router = DefaultRouter()
router.register('stores', StoreViewSet)
router.register('orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth')
]