from django import forms
from .models import Platillo

class MenuForm(forms.ModelForm):
    class Meta:
        model = Platillo
        fields = ['nombre', 'descripcion', 'precio', 'disponible', 'ingredientes', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
            }),
            'descripcion': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'disponible': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
                'role': 'switch'
            }),
            'ingredientes': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
            }),
            'imagen': forms.FileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'
            })
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['precio'].widget.attrs.update({'class': 'form-control'})
