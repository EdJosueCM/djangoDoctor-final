from django.forms import ModelForm, ValidationError
from django import forms
from aplication.core.models import Doctor

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = [
            'nombres', 'apellidos', 'cedula', 'fecha_nacimiento', 'direccion', 
            'latitud', 'longitud', 'especialidad', 'telefonos', 'email', 
            'horario_atencion', 'duracion_cita', 'curriculum', 'foto', 'activo',
            'imagen_receta', 'firmaDigital'
        ]
        
        error_messages = {
            "nombre": {"required": "El nombre es requerido"},
            "apellido": {"required": "El apellido es requerido"},
            "cedula": {
                "required": "La cédula es requerida",
                "unique": "La cédula ya existe"
            },
            "fecha_nacimiento": {"required": "La fecha de nacimiento es requerida"},
            "direccion": {"required": "La dirección es requerida"},
            "latitud": {"required": "La latitud es requerida"},
            "longitud": {"required": "La longitud es requerida"},
            "especialidad": {"required": "La especialidad es requerida"},
            "telefono": {"required": "El teléfono es requerido"},
            "email": {
                "required": "El correo electrónico es requerido",
                "unique": "El correo electrónico ya existe"
            },
            "horario_atencion": {"required": "El horario de atención es requerido"},
            "durac_cita": {"required": "La duración de la cita es requerida"},
            "curriculum": {"required": "El currículum es requerido"},
            "foto": {"required": "La foto es requerida"},
            "estado": {"required": "El estado es requerido"},
            "imagen_receta": {"required": "La imagen de receta es requerida"},
            "firmaDigital": {"required": "La firma digital es requerida"},
        }
        
        widgets = {
            "nombres": forms.TextInput(attrs={
                "placeholder": "Ingrese nombre",
                "id": "id_nombre",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "apellidos": forms.TextInput(attrs={
                "placeholder": "Ingrese apellido",
                "id": "id_apellido",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                

            }),
            "cedula": forms.TextInput(attrs={
                "placeholder": "Ingrese cédula",
                "id": "id_cedula",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "fecha_nacimiento": forms.DateInput(attrs={
                "type": "date",
                "id": "id_fecha_nacimiento",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "direccion": forms.TextInput(attrs={
                "placeholder": "Ingrese dirección",
                "id": "id_direccion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "latitud": forms.TextInput(attrs={
                "placeholder": "Ingrese latitud",
                "id": "id_latitud",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "longitud": forms.TextInput(attrs={
                "placeholder": "Ingrese longitud",
                "id": "id_longitud",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "especialidad": forms.SelectMultiple(attrs={
                "id": "id_especialidad",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "telefonos": forms.TextInput(attrs={
                "placeholder": "Ingrese teléfono",
                "id": "id_telefono",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "email": forms.EmailInput(attrs={
                "placeholder": "Ingrese correo electrónico",
                "id": "id_email",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "horario_atencion": forms.TextInput(attrs={
                "placeholder": "Ingrese horario de atención",
                "id": "id_horario_atencion",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "duracion_cita": forms.NumberInput(attrs={
                "placeholder": "Ingrese duración de la cita",
                "id": "id_duracion_cita",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "curriculum": forms.FileInput(attrs={
                "id": "id_curriculum",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "foto": forms.FileInput(attrs={
                "id": "id_foto",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "estado": forms.Select(attrs={
                "id": "id_estado",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
            "imagen_receta": forms.FileInput(attrs={
                "id": "id_imagen_receta",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
                "onchange": "previewImage(event, 'imagen_receta_preview')",
            }),
            "firmaDigital": forms.FileInput(attrs={
                "id": "id_firmaDigital",
                "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
            }),
        }
