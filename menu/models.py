from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator

class Platillo(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre del platillo")
    descripcion = models.TextField(verbose_name="Descripción", blank=True)
    imagen = models.ImageField(upload_to='platillos/', blank=True, null=True)  
    precio = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Precio"
    )
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    ingredientes = models.TextField(verbose_name="Ingredientes principales", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    class Meta:
        verbose_name = 'platillo'
        verbose_name_plural = 'platillos'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('menu:detalle_platillo', args=[str(self.id)])

