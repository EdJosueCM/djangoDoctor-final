from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import TipoCategoria

class TypeCategoryForm(ModelForm):
    class Meta:
        model = TipoCategoria
        fields = ['categoria_examen', 'nombre', 'descripcion', 'valor_minimo', 'valor_maximo', 'activo']
        
        error_messages = {
            'categoria_examen': {
                'required': "El campo categoría del examen es requerido"
            },
            'nombre': {
                'required': "El campo nombre es requerido"
            },
            'valor_minimo': {
                'required': "El campo valor mínimo es requerido"
            },
            'valor_maximo': {
                'required': "El campo valor máximo es requerido"
            }
        }
        
        widgets = {
            'categoria_examen': forms.Select(
                attrs={
                    "id": "id_categoria_examen",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre",
                    "id": "id_nombre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese descripción",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'valor_minimo': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese valor mínimo",
                    "id": "id_valor_minimo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'valor_maximo': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese valor máximo",
                    "id": "id_valor_maximo",
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

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        if not nombre or len(nombre) < 2:
            raise ValidationError("El campo nombre debe tener al menos 2 caracteres")
        return nombre.capitalize()

    def clean_valor_minimo(self):
        valor_minimo = self.cleaned_data.get('valor_minimo')
        if not valor_minimo or len(valor_minimo) < 1:
            raise ValidationError("El campo valor mínimo debe tener al menos 1 caracter")
        return valor_minimo

    def clean_valor_maximo(self):
        valor_maximo = self.cleaned_data.get('valor_maximo')
        if not valor_maximo or len(valor_maximo) < 1:
            raise ValidationError("El campo valor máximo debe tener al menos 1 caracter")
        return valor_maximo