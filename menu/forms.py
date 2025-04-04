from django import forms
from .models import Platillo

class MenuForm(forms.ModelForm):
    class Meta:
        model = Platillo
        fields = ['nombre', 'descripcion', 'precio', 'disponible', 'ingredientes', 'imagen']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'ingredientes': forms.Textarea(attrs={'rows': 3}),
        }
