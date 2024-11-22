from django import forms
from aplication.attention.models import CostosAtencion, CostoAtencionDetalle, ServiciosAdicionales, Atencion

class CostosAtencionForm(forms.ModelForm):
    class Meta:
        model = CostosAtencion
        fields = ['atencion']
        widgets = {
            'atencion': forms.Select(attrs={'class': 'form-control'}),
        }

class CostoAtencionDetalleForm(forms.ModelForm):
    class Meta:
        model = CostoAtencionDetalle
        fields = ['servicios_adicionales', 'costo_servicio']
        widgets = {
            'servicios_adicionales': forms.Select(attrs={'class': 'form-control'}),
            'costo_servicio': forms.NumberInput(attrs={'class': 'form-control', 'readonly': True}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['servicios_adicionales'].queryset = ServiciosAdicionales.objects.filter(activo=True)