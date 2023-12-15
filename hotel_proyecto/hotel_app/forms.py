from django import forms
from .models import Reserva

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['huesped', 'fecha_llegada', 'fecha_salida', 'tipo_pago', 'tipo_habitacion']
        widgets = {
            'fecha_llegada': forms.TextInput(attrs={'type': 'text'}), 
            'fecha_salida': forms.TextInput(attrs={'type': 'text'}),
        }