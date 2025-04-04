# Generated by Django 5.2 on 2025-04-04 00:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '0002_delete_menuitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Platillo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre del platillo')),
                ('descripcion', models.TextField(blank=True, verbose_name='Descripción')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Precio')),
                ('disponible', models.BooleanField(default=True, verbose_name='Disponible')),
                ('ingredientes', models.TextField(blank=True, verbose_name='Ingredientes principales')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'platillo',
                'verbose_name_plural': 'platillos',
                'ordering': ['nombre'],
            },
        ),
    ]
