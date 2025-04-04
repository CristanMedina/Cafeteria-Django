from django.db import models
from django.conf import settings
from menu.models import Dish

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('preparing', 'En preparación'),
        ('finished', 'Terminada'),
        ('delivered', 'Entregada'),
    ]
    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    notes = models.TextField(blank=True, null=True)
