from django.db import models
from django.contrib.auth import get_user_model


class Store(models.Model):
    title = models.CharField(max_length=50, null=False, blank=False, verbose_name="Заголовок")
    price = models.CharField(max_length=20, blank=False, null=False, verbose_name='Цена')
    seller = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='stores',
                               verbose_name="Продавец")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return f'{self.pk}. {self.title}'


class Order(models.Model):
    phone = models.CharField(max_length=10, null=False, blank=False, verbose_name='Номер')
    address = models.CharField(max_length=100, null=False, blank=False, verbose_name='Адресс')
    store = models.ForeignKey('webapp.Store', on_delete=models.CASCADE, related_name='orders', default=1)
    customer = models.ForeignKey(get_user_model(), on_delete=models.SET_DEFAULT, default=1, related_name='customers',
                                 verbose_name="Клиент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return f'{self.pk}. {self.address[:20]}'