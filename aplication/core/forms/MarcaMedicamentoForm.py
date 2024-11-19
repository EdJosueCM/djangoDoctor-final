from django import forms
from django.forms import ModelForm, ValidationError
from aplication.core.models import MarcaMedicamento

class MarcaMedicamentoForm(ModelForm):
    class Meta:
        model = MarcaMedicamento
        fields = ['nombre', 'descripcion', 'activo']
        
        error_messages = {
            'nombre': {
                'required': "El campo nombre es requerido",
                'unique': "Esta marca de medicamento ya existe",
            },
        }
        
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese la marca",
                    "id": "id_nombre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'descripcion': forms.Textarea(
                attrs={
                    "placeholder": "Ingrese descripción",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                    "rows": 3,
                }
            ),
            'activo': forms.CheckboxInput(
                attrs={
                    "id": "id_activo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 dark:bg-principal dark:border-gray-600 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if len(nombre) < 2:
            raise ValidationError("El campo nombre debe tener al menos 2 caracteres")
        return nombre.capitalize()
