# Generated by Django 5.2 on 2025-04-03 23:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orders', '0002_rename_comida_menuitem_nombre_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='KitchenOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
            ],
        ),
    ]
