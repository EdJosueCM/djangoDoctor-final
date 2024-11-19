from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Permission
from django.db.models.signals import post_migrate
from aplication.core.models import Doctor

from aplication.security.models import User

# @receiver(post_save, sender=User)

# def assign_user_group(sender, instance, created, **kwargs):
#     if created:
#         if instance.is_superuser:
#             print(instance)
#             admin_group, created = Group.objects.get_or_create(name='Administradores')
#             instance.groups.add(admin_group)
#             Customer.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, dni=instance.dni, email=instance.email, phone=instance.phone)
#         else:
#             client_group, created = Group.objects.get_or_create(name='Clientes')
#             instance.groups.add(client_group)
#             Customer.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, dni=instance.dni, email=instance.email, phone=instance.phone)

@receiver(post_save, sender=User)
def assign_doctor_group(sender, instance, created, **kwargs):
    if created:
        # Si el usuario es un doctor, asignar el grupo y crear la instancia de Doctor
        if instance.is_staff and not instance.is_superuser:  # Puedes ajustar esta condición según tus necesidades
            doctor_group, group_created = Group.objects.get_or_create(name='Doctores')
            instance.groups.add(doctor_group)
            
            # Crear una instancia de Doctor asociada al usuario
            Doctor.objects.create(
                nombres=instance.first_name,
                apellidos=instance.last_name,
                cedula=instance.dni,  # Ajusta si `dni` no está en `User`
                direccion="",
                email=instance.email,
                telefonos=instance.phone
            )


# @receiver(post_save, sender=User)
# def asignar_permisos(sender, instance, created, **kwargs):
#     if created:
#         if instance.groups.filter(name='Administradores').exists():
#             administradores = Group.objects.get(name='Administradores')
#             permisos_administradores = Permission.objects.all()
#             administradores.permissions.set(permisos_administradores)
#         elif instance.groups.filter(name='Clientes').exists():
#             # Aquí podrías asignar permisos específicos para clientes si lo necesitas
#             pass