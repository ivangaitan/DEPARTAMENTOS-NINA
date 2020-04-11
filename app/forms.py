from django import forms
from .models import *       

class ReservaForm(forms.ModelForm):
    
    class Meta:
        model = Reserva
        fields = ('dia_inicial', 'dia_final',)
