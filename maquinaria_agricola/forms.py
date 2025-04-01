from django import forms
from .models import Maquina, Complemento, Trabajador, Operacion

class MaquinaForm(forms.ModelForm):
    class Meta:
        model = Maquina
        fields = '__all__'

class ComplementoForm(forms.ModelForm):
    class Meta:
        model = Complemento
        fields = '__all__'

class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'

class OperacionForm(forms.ModelForm):
    class Meta:
        model = Operacion
        fields = '__all__'
        widgets = {
            'fecha_entrada': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_salida': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }