from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Cliente

class ClienteRegistrationForm(UserCreationForm):
    class Meta:
        model = Cliente
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        cliente = super().save(commit=False)
        cliente.role = Cliente.base_role
        if commit:
            cliente.save()
        return cliente
