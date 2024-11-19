from django.forms import ModelForm, Textarea, TextInput, CheckboxInput
from django import forms
from aplication.core.models import TipoMedicamento


class TipoMedicamentoForm(ModelForm):
    class Meta:
        model = TipoMedicamento
        fields = ["nombre", "descripcion", "activo"]

        error_messages = {
            "nombre": {"required": "El nombre del tipo de medicamento es requerido"},
            "descripcion": {"required": "La descripción es requerida"},
            "activo": {"required": "El estado activo es requerido"},
        }

        widgets = {
            "nombre": TextInput(
                attrs={
                    "placeholder": "Ingrese nombre del tipo de medicamento",
                    "id": "id_nombre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "descripcion": Textarea(
                attrs={
                    "placeholder": "Ingrese descripción del tipo de medicamento",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "activo": CheckboxInput(
                attrs={
                    "id": "id_activo",
                    "class": "shadow-sm focus:ring-blue-500 focus:border-blue-500",
                }
            ),
        }
