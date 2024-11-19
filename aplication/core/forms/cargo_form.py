from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import Cargo


class CargoForm(ModelForm):
    class Meta:
        model = Cargo
        fields = ["nombre", "descripcion", "activo"]

        error_messages = {
            "nombre": {"required": "El campo nombre es requerido"},
        }

        widgets = {
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre del cargo",
                    "id": "id_nombre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese descripción del cargo",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                    "rows": 4,
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "id": "id_activo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        if not nombre or len(nombre) < 2:
            raise ValidationError("El campo nombre debe tener al menos 2 caracteres")
        return nombre.capitalize()

    def clean_descripcion(self):
        descripcion = self.cleaned_data.get("descripcion")
        if descripcion and len(descripcion) < 5:
            raise ValidationError("La descripción debe tener al menos 5 caracteres")
        return descripcion
