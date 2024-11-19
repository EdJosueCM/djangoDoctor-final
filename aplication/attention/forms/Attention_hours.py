# Description: Formulario para el modelo HorarioAtencion
from django.forms import ModelForm, ValidationError
from django import forms
from aplication.attention.models import HorarioAtencion

class AttentionHoursForm(ModelForm):
    class Meta:
        model = HorarioAtencion
        fields = ['dia_semana', 'hora_inicio', 'hora_fin', 'Intervalo_desde', 'Intervalo_hasta', 'activo']
        
        error_messages = {
            'dia_semana': {
                'required': "El campo día de la semana es requerido"
            },
            'hora_inicio': {
                'required': "El campo hora de inicio es requerido"
            },
            'hora_fin': {
                'required': "El campo hora de fin es requerido"
            },
            'Intervalo_desde': {
                'required': "El campo intervalo desde es requerido"
            },
            'Intervalo_hasta': {
                'required': "El campo intervalo hasta es requerido"
            },
            'activo': {
                'required': "El campo activo es requerido"
            }
        }
        
        widgets = {
            'dia_semana': forms.Select(
                attrs={
                    "id": "id_dia_semana",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'hora_inicio': forms.TimeInput(
                attrs={
                    "placeholder": "Ingrese hora de inicio",
                    "id": "id_hora_inicio",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'hora_fin': forms.TimeInput(
                attrs={
                    "placeholder": "Ingrese hora de fin",
                    "id": "id_hora_fin",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'Intervalo_desde': forms.TimeInput(
                attrs={
                    "placeholder": "Ingrese intervalo desde",
                    "id": "id_intervalo_desde",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'Intervalo_hasta': forms.TimeInput(
                attrs={
                    "placeholder": "Ingrese intervalo hasta",
                    "id": "id_intervalo_hasta",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
            'activo': forms.CheckboxInput(
                attrs={
                    "id": "id_activo",
                    "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                }
            ),
        }

    def clean_hora_inicio(self):
        hora_inicio = self.cleaned_data.get('hora_inicio')
        if not hora_inicio:
            raise ValidationError("El campo hora de inicio es requerido")
        return hora_inicio

    def clean_hora_fin(self):
        hora_fin = self.cleaned_data.get('hora_fin')
        if not hora_fin:
            raise ValidationError("El campo hora de fin es requerido")
        return hora_fin

    def clean_Intervalo_desde(self):
        Intervalo_desde = self.cleaned_data.get('Intervalo_desde')
        if not Intervalo_desde:
            raise ValidationError("El campo intervalo desde es requerido")
        return Intervalo_desde

    def clean_Intervalo_hasta(self):
        Intervalo_hasta = self.cleaned_data.get('Intervalo_hasta')
        if not Intervalo_hasta:
            raise ValidationError("El campo intervalo hasta es requerido")
        return Intervalo_hasta 
    