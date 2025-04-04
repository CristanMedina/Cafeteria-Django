from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        COCINERO = 'COCINERO', 'Cocinero'
        CLIENTE = 'CLIENTE', 'Cliente'

    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.CLIENTE
    )

    def save(self, *args, **kwargs):
        if self.role in [User.Role.ADMIN, User.Role.COCINERO]:
            self.is_staff = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
