from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import Diagnostico

class DiagnosisForm(ModelForm): 
    class Meta:
        model = Diagnostico
        fields = ['codigo', 'descripcion', 'datos_adicionales', 'activo']
        
        error_messages = {
            'codigo': {
                'required': "El campo codigo es requerido"
            },
            'descripcion': {
                'required': "El campo descripcion es requerido"
            }
        }
        
        widgets = {
            'codigo': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese codigo",
                    "id": "id_codigo",
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
            'datos_adicionales': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese datos adicionales",
                    "id": "id_datos_adicionales",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'activo': forms.CheckboxInput(
                attrs={
                    "id": "id_activo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }

    def clean_codigo(self):
        codigo = self.cleaned_data.get('codigo')
        if not codigo or len(codigo) < 2:
            raise ValidationError("El campo codigo debe tener al menos 2 caracteres")
        return codigo.upper()

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get('descripcion')
        if not descripcion or len(descripcion) < 2:
            raise ValidationError("El campo descripcion debe tener al menos 2 caracteres")
        return descripcion.capitalize()