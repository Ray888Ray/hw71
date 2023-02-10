from webapp.views import index
from django.urls import path

app_name = 'webapp'


urlpatterns = [
    path('', index, name='index'),
]