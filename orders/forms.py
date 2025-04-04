from django import forms
from .models import Order
from menu.models import Platillo

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['platillo', 'quantity', 'pickup_name', 'special_requests']
        widgets = {
            'quantity': forms.NumberInput(attrs={'min': 1, 'class': 'form-control'}),
            'pickup_name': forms.TextInput(attrs={'class': 'form-control'}),
            'special_requests': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'platillo': forms.Select(attrs={'class': 'form-select'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['platillo'].queryset = Platillo.objects.filter(disponible=True)
        self.fields['quantity'].initial = 1
