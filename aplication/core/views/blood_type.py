from django.urls import reverse_lazy
from aplication.core.forms.blood_type import BloodTypeForm
from aplication.core.models import TipoSangre
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class BloodTypeListView(ListView):
    template_name = "core/blood_type/list.html"
    model = TipoSangre
    context_object_name = 'Tipos_Sangre'
    query = None
    paginate_by = 5
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q') # ver
        if q1 is not None: 
            self.query |= Q(tipo__icontains=q1) 
            self.query |= Q(descripcion__icontains=q1)  
        return self.model.objects.filter(self.query).order_by('tipo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Tipos de Sangre"
        return context
    

class BloodTypeCreateView(CreateView):
    model = TipoSangre
    template_name = 'core/blood_type/form.html'
    form_class = BloodTypeForm
    success_url = reverse_lazy('core:blood_type_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Tipos de Sangre'
        context['grabar'] = 'Grabar Tipo de Sangre'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        blood_type = self.object
        save_audit(self.request, blood_type, action='A')
        messages.success(self.request, f"Éxito al crear el tipo de sangre {blood_type.tipo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class BloodTypeUpdateView(UpdateView):
    model = TipoSangre
    template_name = 'core/blood_type/form.html'
    form_class = BloodTypeForm
    success_url = reverse_lazy('core:blood_type_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Actualización de Tipos de Sangre'
        context['grabar'] = 'Actualizar Tipo de Sangre'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        blood_type = self.object
        save_audit(self.request, blood_type, action='M')
        messages.success(self.request, f"Éxito al actualizar el tipo de sangre {blood_type.tipo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class BloodTypeDeleteView(DeleteView):
    model = TipoSangre
    template_name = 'core/blood_type/delete.html'
    success_url = reverse_lazy('core:blood_type_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Tipo de Sangre'
        context['grabar'] = f'¿Está seguro de eliminar el tipo de sangre {self.object.tipo}?'
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        blood_type = self.get_object()
        save_audit(request, blood_type, action='E')
        messages.success(request, f"Éxito al eliminar el tipo de sangre {blood_type.nombre}.")
        return super().delete(request, *args, **kwargs)

class BloodTypeDetailView(DetailView):
    model = TipoSangre
    
    def get(self, request, *args, **kwargs):
        blood_type = self.get_object()
        data = {
            'id': blood_type.id,
            'tipo': blood_type.tipo,
            'descripcion': blood_type.descripcion
        }
        return JsonResponse(data)