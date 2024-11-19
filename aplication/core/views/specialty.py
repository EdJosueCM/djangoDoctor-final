from django.urls import reverse_lazy
from aplication.core.forms.specialty import SpecialtyForm
from aplication.core.models import Especialidad
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class SpecialtyListView(ListView):
    model = Especialidad
    template_name = 'core/specialty/list.html'
    context_object_name = 'especialidades'
    paginate_by = 5

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Especialidad.objects.filter(
                Q(nombre__icontains=query) |
                Q(descripcion__icontains=query)
            )
        return Especialidad.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Medical'
        context['title1'] = 'Consulta de especialidades'
        return context

class SpecialtyCreateView(CreateView):
    model = Especialidad
    form_class = SpecialtyForm
    template_name = 'core/specialty/form.html'
    success_url = reverse_lazy('core:specialty_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Registro de especialidad'
        context['grabar'] = 'Grabar especialidad'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action='A')
        messages.success(self.request, f'Éxito al crear la especialidad {patient.nombre}.')
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error al enviar el formulario. Corrige los errores.')
        return self.render_to_response(self.get_context_data(form=form))
    
class SpecialtyUpdateView(UpdateView):
    model = Especialidad
    form_class = SpecialtyForm
    template_name = 'core/specialty/form.html'
    success_url = reverse_lazy('core:specialty_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Actualización de especialidad'
        context['grabar'] = 'Actualizar especialidad'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        respose = super().form_valid(form)
        patient = self.object
        save_audit(self.request, patient, action='M')
        messages.success(self.request, f'Éxito al actualizar la especialidad {patient.nombre}.')
        return respose
    
    def form_invalid(self, form):
        messages.error(self.request, 'Error al actualizar la especialidad')
        return self.render_to_response(self.get_context_data(form=form))

class SpecialtyDeleteView(DeleteView):
    model = Especialidad
    template_name = 'specialty_delete.html'
    success_url = reverse_lazy('core:specialty_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar especialidad'
        context['message'] = f"¿Está seguro de eliminar la especialidad {self.object.nombre}?"
        return context 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar especialidad'
        context['message'] = f"¿Está seguro de eliminar la especialidad {self.object.nombre}?"
        return context

    def delete(self, request, *args, **kwargs):
        save_audit(self.request, 'Eliminación de especialidad')
        messages.success(self.request, 'Especialidad eliminada con éxito')
        # cambiar estado a eliminado
        # self.object.estado = False
        # self.object.save()
        return super().delete(request, *args, **kwargs)
    
class SpecialtyDetailView(DetailView):
    model = Especialidad
    
    def get_context_data(self, request, **kwargs):
        context = super().get_odject()
        data = {
            'id': context.id,
            'nombre': context.nombre,
            'descripcion': context.descripcion,
            'estado': context.estado
        }
        return JsonResponse(data)