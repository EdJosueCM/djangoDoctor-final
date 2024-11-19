from django.urls import reverse_lazy
from aplication.core.forms.doctor import DoctorForm
from aplication.core.models import Doctor
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class DoctorListView(ListView):
    template_name = "core/doctor/list.html"
    model = Doctor
    context_object_name = 'doctores'
    paginate_by = 2
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query.add(Q(nombres__icontains=q1), Q.OR)
            self.query.add(Q(apellidos__icontains=q1), Q.OR)
            self.query.add(Q(cedula__icontains=q1), Q.OR)
        return self.model.objects.filter(self.query).order_by('apellidos')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Doctores"
        return context
    
class DoctorCreateView(CreateView):
    model = Doctor
    template_name = 'core/doctor/form.html'
    form_class = DoctorForm
    success_url = reverse_lazy('core:doctor_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Doctores'
        context['grabar'] = 'Grabar Doctor'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        doctor = self.object
        save_audit(self.request, doctor, action='A')
        messages.success(self.request, f"Éxito al crear al doctor {doctor.nombre_completo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al Modificar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class DoctorUpdateView(UpdateView): 
    model = Doctor
    template_name = 'core/doctor/form.html'
    form_class = DoctorForm
    success_url = reverse_lazy('core:doctor_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Actualización de Doctores'
        context['grabar'] = 'Actualizar Doctor'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        doctor = self.object
        save_audit(self.request, doctor, action='M')
        messages.success(self.request, f"Éxito al Modificar el doctor {doctor.nombre_completo}.")
        print("mande mensaje")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class DoctorDeleteView(DeleteView):
    model = Doctor
    success_url = reverse_lazy('core:doctor_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Doctor'
        context['description'] = f'¿Está seguro de eliminar el doctor: {self.object.name }?'
        context['back_url'] = self.success_url
    
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar al doctor {self.object.name}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)
    
class DoctorDetailView(DetailView):
    model = Doctor
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        especialidades = list(self.object.especialidad.values('id', 'nombre'))  # Convierte a una lista de diccionarios
        data = {
            'id': self.object.id,
            'nombres': self.object.nombres,
            'apellidos': self.object.apellidos,
            'cedula': self.object.cedula,
            'fecha_nacimiento': self.object.fecha_nacimiento,
            'direccion': self.object.direccion,
            'latitud': self.object.latitud,
            'longitud': self.object.longitud,
            'especialidad': especialidades,
            'telefono': self.object.telefonos,
            'email': self.object.email,
            'horario_atencion': self.object.horario_atencion,
            'duracion_cita': self.object.duracion_cita,
            'curriculum': self.object.curriculum.url if self.object.curriculum else None,  # Convierte a URL
            'foto': self.object.foto.url,  # Convierte a URL
            'activo': self.object.activo
        }
        return JsonResponse(data)