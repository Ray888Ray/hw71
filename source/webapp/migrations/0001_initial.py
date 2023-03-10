# Generated by Django 4.1.6 on 2023-02-09 08:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Заголовок')),
                ('price', models.CharField(max_length=20, verbose_name='Цена')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('seller', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='stores', to=settings.AUTH_USER_MODEL, verbose_name='Продавец')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=10, verbose_name='Номер')),
                ('address', models.CharField(max_length=100, verbose_name='Адресс')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='customers', to=settings.AUTH_USER_MODEL, verbose_name='Клиент')),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='webapp.store')),
            ],
        ),
    ]
