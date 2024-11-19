from django.forms import ModelForm
from django import forms
from aplication.core.models import Medicamento


class MedicamentoForm(ModelForm):
    class Meta:
        model = Medicamento
        fields = [
            "tipo",
            "marca_medicamento",
            "nombre",
            "descripcion",
            "concentracion",
            "cantidad",
            "precio",
            "comercial",
            "activo",
            "foto",
        ]

        error_messages = {
            "tipo": {"required": "El tipo de medicamento es requerido"},
            "marca_medicamento": {"required": "La marca del medicamento es requerida"},
            "nombre": {"required": "El nombre del medicamento es requerido"},
            "cantidad": {"required": "La cantidad es requerida"},
            "precio": {"required": "El precio es requerido"},
            "comercial": {"required": "Especifique si el medicamento es comercial"},
            "activo": {"required": "El estado activo es requerido"},
            "foto": {"required": "La foto es requerida"},
        }

        widgets = {
            "tipo": forms.Select(
                attrs={
                    "id": "id_tipo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "marca_medicamento": forms.Select(
                attrs={
                    "id": "id_marca_medicamento",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "nombre": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese nombre del medicamento",
                    "id": "id_nombre",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "descripcion": forms.Textarea(
                attrs={
                    "placeholder": "Ingrese descripción",
                    "id": "id_descripcion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "concentracion": forms.TextInput(
                attrs={
                    "placeholder": "Ingrese concentración",
                    "id": "id_concentracion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "cantidad": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese cantidad",
                    "id": "id_cantidad",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "precio": forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese precio",
                    "id": "id_precio",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                }
            ),
            "comercial": forms.CheckboxInput(
                attrs={
                    "id": "id_comercial",
                    "class": "shadow-sm focus:ring-blue-500 focus:border-blue-500",
                }
            ),
            "activo": forms.CheckboxInput(
                attrs={
                    "id": "id_activo",
                    "class": "shadow-sm focus:ring-blue-500 focus:border-blue-500",
                }
            ),
            "foto": forms.FileInput(
                attrs={
                    "id": "id_foto",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5",
                    "onchange": "previewImage(event, 'foto_preview')",
                }
            ),
        }
