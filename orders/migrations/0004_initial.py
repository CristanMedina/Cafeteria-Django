# Generated by Django 5.2 on 2025-04-04 01:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0003_initial'),
        ('orders', '0003_remove_order_items_delete_menuitem_delete_order'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('special_requests', models.TextField(blank=True, null=True)),
                ('pickup_name', models.CharField(help_text='Nombre para identificar el pedido', max_length=100)),
                ('status', models.CharField(choices=[('P', 'Pendiente'), ('EP', 'En proceso'), ('T', 'Terminado'), ('E', 'Entregado'), ('C', 'Cancelado')], default='P', max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('platillo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.platillo')),
            ],
            options={
                'verbose_name': 'pedido',
                'verbose_name_plural': 'pedidos',
                'ordering': ['-created_at'],
            },
        ),
    ]
