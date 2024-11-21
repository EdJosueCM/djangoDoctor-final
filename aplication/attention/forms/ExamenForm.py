from django import forms
from aplication.attention.models import Examen

class ExamenForm(forms.ModelForm):
    class Meta:
        model = Examen
        fields = ['atencion', 'tipo_examen', 'doctor', 'estado', 
                 'descripcion', 'archivo_resultado', 'observaciones_doctor']
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}),
            'observaciones_doctor': forms.Textarea(attrs={'rows': 3}),
        }