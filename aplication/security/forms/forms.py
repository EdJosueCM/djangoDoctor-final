from django import forms
from django.contrib.auth import get_user_model
from aplication.security.models import User

User = get_user_model()

class UpdateProfileForm(forms.ModelForm):
    current_password = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password1 = forms.CharField(widget=forms.PasswordInput(), required=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput(), required=False)

    class Meta:
        model = User
        fields = [
            'username', 'first_name', 'last_name', 'dni', 'phone', 'email', 'image', 
            'direction'
        ]
        widgets = {
            "image": forms.FileInput(
                attrs={
                    "type": "file",
                    "id": "dropzone-file",
                    "class": "hidden",
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance:
            self.fields['first_name'].initial = self.instance.first_name
            self.fields['last_name'].initial = self.instance.last_name
            self.fields['email'].initial = self.instance.email
            self.fields['phone'].initial = self.instance.phone
            self.fields['dni'].initial = self.instance.dni
            self.fields['direction'].initial = self.instance.direction
            self.fields['image'].initial = self.instance.image

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from aplication.security.models import User, Menu, Module, GroupModulePermission
from django.forms import ModelForm

class ProfileUserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'dni', 'phone', 'direction', 'image']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
            'username': 'Nombre de usuario',
            'dni': 'Cédula o RUC',
            'phone': 'Teléfono',
            'direction': 'Dirección',
            'image': 'Imagen de perfil',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'dni': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'direction': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. Introduce una dirección de correo válida.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email ya está registrado.')
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        fields = "__all__"
        
class ModuloForm(ModelForm):
    class Meta:
        model = Module
        fields = "__all__"
        
class GroupModulePermissionForm(ModelForm):
    class Meta:
        model = GroupModulePermission
        fields = "__all__"
        