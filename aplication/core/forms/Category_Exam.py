# from django.forms import ModelForm, ValidationError
# from django import forms
# from aplication.core.models import CategoriaExamen

# class CategoryExamForm(ModelForm):
#     class Meta:
#         model = CategoriaExamen
#         fields = ['nombre', 'descripcion', 'activo']
        
#         error_messages = {
#             'nombre': {
#                 'required': "El campo nombre es requerido"
#             },
#             'descripcion': {
#                 'required': "El campo descripcion es requerido"
#             }
#         }
        
#         widgets = {
#             'nombre': forms.TextInput(
#                 attrs={
#                     "placeholder": "Ingrese nombre",
#                     "id": "id_nombre",
#                     "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
#                 }
#             ),
#             'descripcion': forms.TextInput(
#                 attrs={
#                     "placeholder": "Ingrese descripcion",
#                     "id": "id_descripcion",
#                     "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
#                 }
#             ),
#             'activo': forms.CheckboxInput(
#                 attrs={
#                     "id": "id_activo",
#                     "class": "shadow-sm bg-gray-50 border border-gray-300 text-gray-900 rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 pr-12 dark:bg-principal dark:border-gray-600 dark:placeholder-gray-400 dark:text-gray-400 dark:focus:ring-blue-500 dark:focus:border-blue-500 dark:shadow-sm-light",
#                 }
#             ),
#         }

#     def clean_nombre(self):
#         nombre = self.cleaned_data.get('nombre')
#         if not nombre or len(nombre) < 2:
#             raise ValidationError("El campo nombre debe tener al menos 2 caracteres")
#         return nombre.capitalize()

#     def clean_descripcion(self):
#         descripcion = self.cleaned_data.get('descripcion')
#         if not descripcion or len(descripcion) < 2:
#             raise ValidationError("El campo descripcion debe tener al menos 2 caracteres")
#         return descripcion.capitalize()