from django.db import models
from users.models import User
from menu.models import Platillo

class Order(models.Model):
    class Status(models.TextChoices):
        PENDIENTE = 'P', 'Pendiente'
        EN_PROCESO = 'EP', 'En proceso'
        TERMINADO = 'T', 'Terminado'
        ENTREGADO = 'E', 'Entregado'
        CANCELADO = 'C', 'Cancelado'

    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    platillo = models.ForeignKey(Platillo, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    special_requests = models.TextField(blank=True, null=True)
    pickup_name = models.CharField(max_length=100, help_text="Nombre para identificar el pedido")
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.PENDIENTE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order #{self.id} - {self.platillo.nombre}"

    def total_price(self):
        return self.platillo.precio * self.quantity

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'pedido'
        verbose_name_plural = 'pedidos'
