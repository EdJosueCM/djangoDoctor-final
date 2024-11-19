from django.forms import ModelForm, ValidationError
from django import forms
from aplication.attention.models import ServiciosAdicionales

class AdditionalServicesForm(ModelForm):
    class Meta:
        model = ServiciosAdicionales
        fields = ['nombre_servicio', 'costo_servicio', 'descripcion', 'activo']
        
        error_messages = {
            'nombre_servicio': {
                'required': "El nombre del servicio es requerido"
            },
            'costo_servicio': {
                'required': "El costo del servicio es requerido"
            }
        }
        
        widgets = {
            'nombre_servicio': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre del servicio",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'costo_servicio': forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese costo del servicio",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    "placeholder": "Ingrese descripción del servicio",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'activo': forms.CheckboxInput(
                attrs={
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            )
        }

    def clean_nombre_servicio(self):
        nombre_servicio = self.cleaned_data.get('nombre_servicio')
        if not nombre_servicio:
            raise ValidationError("El nombre del servicio es requerido")
        return nombre_servicio

    def clean_costo_servicio(self):
        costo_servicio = self.cleaned_data.get('costo_servicio')
        if not costo_servicio:
            raise ValidationError("El costo del servicio es requerido")
        return costo_servicio