from django.urls import reverse_lazy
from aplication.core.forms.diagnosis import DiagnosisForm
from aplication.core.models import Diagnostico
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class DiagnosisListView(ListView):
    template_name = "core/diagnosis/list.html"
    model = Diagnostico
    context_object_name = 'Diagnosticos'
    query = None
    paginate_by = 5
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q') # ver
        if q1 is not None: 
            self.query |= Q(codigo__icontains=q1) 
            self.query |= Q(descripcion__icontains=q1)  
        return self.model.objects.filter(self.query).order_by('codigo')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Diagnósticos"
        return context

class DiagnosisCreateView(CreateView):
    model = Diagnostico
    template_name = 'core/diagnosis/form.html'
    form_class = DiagnosisForm
    success_url = reverse_lazy('core:diagnosis_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Diagnósticos'
        context['grabar'] = 'Grabar Diagnóstico'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        diagnosis = self.object
        save_audit(self.request, diagnosis, action='A')
        messages.success(self.request, f"Éxito al crear el diagnóstico {diagnosis.codigo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class DiagnosisUpdateView(UpdateView):
    model = Diagnostico
    template_name = 'core/diagnosis/form.html'
    form_class = DiagnosisForm
    success_url = reverse_lazy('core:diagnosis_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Actualización de Diagnósticos'
        context['grabar'] = 'Actualizar Diagnóstico'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        diagnosis = self.object
        save_audit(self.request, diagnosis, action='M')
        messages.success(self.request, f"Éxito al actualizar el diagnóstico {diagnosis.codigo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class DiagnosisDeleteView(DeleteView):
    model = Diagnostico
    template_name = 'core/diagnosis/delete.html'
    success_url = reverse_lazy('core:diagnosis_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Diagnóstico'
        context['grabar'] = f'¿Está seguro de eliminar el diagnóstico {self.object.codigo}?'
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        diagnosis = self.get_object()
        save_audit(request, diagnosis, action='E')
        messages.success(request, f"Éxito al eliminar el diagnóstico {diagnosis.codigo}.")
        return super().delete(request, *args, **kwargs)

class DiagnosisDetailView(DetailView):
    model = Diagnostico
    
    def get(self, request, *args, **kwargs):
        diagnosis = self.get_object()
        data = {
            'id': diagnosis.id,
            'codigo': diagnosis.codigo,
            'descripcion': diagnosis.descripcion,
            'datos_adicionales': diagnosis.datos_adicionales,
        }
        return JsonResponse(data)
