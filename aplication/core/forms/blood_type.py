from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import TipoSangre

class BloodTypeForm(ModelForm):
    class Meta:
        model = TipoSangre
        fields = ['tipo', 'descripcion']
        
        error_messages = {
            'tipo': {
                'required': "El campo tipo es requerido"
            },
            'descripcion': {
                'required': "El campo descripcion es requerido"
            }
        }
        
        widgets = {
            'tipo': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese tipo",
                    "id": "id_tipo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese descripcion",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }

    def clean_tipo(self):
        tipo = self.cleaned_data.get('tipo')
        if not tipo or len(tipo) < 2:
            raise ValidationError("El campo tipo debe tener al menos 2 caracteres")
        return tipo.upper()

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not descripcion or len(descripcion) < 2:
            raise ValidationError("El campo descripcion debe tener al menos 2 caracteres")
        return descripcion.capitalize()
