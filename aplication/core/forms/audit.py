from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import AuditUser

class AuditUserForm(ModelForm):
    class Meta:
        model = AuditUser
        fields = ['usuario', 'tabla', 'registroid', 'accion', 'fecha', 'hora', 'estacion']
        
        error_messages = {
            'usuario': {
                'required': "El campo usuario es requerido"
            },
            'tabla': {
                'required': "El campo tabla es requerido"
            },
            'registroid': {
                'required': "El campo registroid es requerido"
            },
            'accion': {
                'required': "El campo accion es requerido"
            },
            'fecha': {
                'required': "El campo fecha es requerido"
            },
            'hora': {
                'required': "El campo hora es requerido"
            },
            'estacion': {
                'required': "El campo estacion es requerido"
            }
        }
        
        widgets = {
            'usuario': forms.Select(
                attrs={
                    "id": "id_usuario",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'tabla': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese tabla",
                    "id": "id_tabla",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'registroid': forms.NumberInput(
                attrs={
                    "placeholder": "Ingrese registroid",
                    "id": "id_registroid",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'accion': forms.Select(
                attrs={
                    "id": "id_accion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'fecha': forms.DateInput(
                attrs={
                    "placeholder": "Ingrese fecha",
                    "id": "id_fecha",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'hora': forms.TimeInput(
                attrs={
                    "placeholder": "Ingrese hora",
                    "id": "id_hora",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'estacion': forms.TextInput(
                attrs={
                    "placeholder": "Ingrese estacion",
                    "id": "id_estacion",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }

    def clean_tabla(self):
        tabla = self.cleaned_data.get('tabla')
        if not tabla or len(tabla) < 2:
            raise ValidationError("El campo tabla debe tener al menos 2 caracteres")
        return tabla.capitalize()

    def clean_estacion(self):
        estacion = self.cleaned_data.get('estacion')
        if not estacion or len(estacion) < 2:
            raise ValidationError("El campo estacion debe tener al menos 2 caracteres")
        return estacion.capitalize()