from django.urls import reverse_lazy
from aplication.attention.forms.Additional_services import AdditionalServicesForm
from aplication.attention.models import ServiciosAdicionales
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class AdditionalServicesListView(ListView):
    template_name = "attention/additional_services/list.html"
    model = ServiciosAdicionales
    context_object_name = 'Servicios_Adicionales'
    query = None
    paginate_by = 5
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')
        if q1 is not None: 
            self.query |= Q(nombre_servicio__icontains=q1) 
            self.query |= Q(descripcion__icontains=q1)  
        return self.model.objects.filter(self.query).order_by('nombre_servicio')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Servicios Adicionales"
        return context
    

class AdditionalServicesCreateView(CreateView):
    model = ServiciosAdicionales
    template_name = 'attention/additional_services/form.html'
    form_class = AdditionalServicesForm
    success_url = reverse_lazy('attention:additional_services_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Servicios Adicionales'
        context['grabar'] = 'Grabar Servicio Adicional'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        additional_service = self.object
        save_audit(self.request, additional_service, action='A')
        messages.success(self.request, f"Éxito al crear el servicio adicional {additional_service.nombre_servicio}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class AdditionalServicesUpdateView(UpdateView):
    model = ServiciosAdicionales
    template_name = 'attention/additional_services/form.html'
    form_class = AdditionalServicesForm
    success_url = reverse_lazy('attention:additional_services_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Actualización de Servicios Adicionales'
        context['grabar'] = 'Actualizar Servicio Adicional'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        additional_service = self.object
        save_audit(self.request, additional_service, action='M')
        messages.success(self.request, f"Éxito al actualizar el servicio adicional {additional_service.nombre_servicio}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class AdditionalServicesDeleteView(DeleteView):
    model = ServiciosAdicionales
    template_name = 'attention/additional_services/delete.html'
    success_url = reverse_lazy('attention:additional_services_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Servicio Adicional'
        context['grabar'] = f'¿Está seguro de eliminar el servicio adicional {self.object.nombre_servicio}?'
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        additional_service = self.get_object()
        save_audit(request, additional_service, action='E')
        messages.success(request, f"Éxito al eliminar el servicio adicional {additional_service.nombre_servicio}.")
        return super().delete(request, *args, **kwargs)

class AdditionalServicesDetailView(DetailView):
    model = ServiciosAdicionales
    
    def get(self, request, *args, **kwargs):
        additional_service = self.get_object()
        data = {
            'id': additional_service.id,
            'nombre_servicio': additional_service.nombre_servicio,
            'costo_servicio': additional_service.costo_servicio,
            'descripcion': additional_service.descripcion,
            'activo': additional_service.activo
        }
        return JsonResponse(data)
