from django.urls import reverse_lazy
from aplication.attention.forms.Attention_hours import AttentionHoursForm
from aplication.attention.models import HorarioAtencion
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class AttentionHoursListView(ListView):
    template_name = "attention/attention_hours/list.html"
    model = HorarioAtencion
    context_object_name = 'Horarios_Atencion'
    query = None
    paginate_by = 5
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')
        if q1 is not None: 
            self.query |= Q(dia_semana__icontains=q1) 
            self.query |= Q(hora_inicio__icontains=q1)  
        return self.model.objects.filter(self.query).order_by('dia_semana')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Horarios de Atención"
        return context
    

class AttentionHoursCreateView(CreateView):
    model = HorarioAtencion
    template_name = 'attention/attention_hours/form.html'
    form_class = AttentionHoursForm
    success_url = reverse_lazy('attention:attention_hours_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Horarios de Atención'
        context['grabar'] = 'Grabar Horario de Atención'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        attention_hours = self.object
        save_audit(self.request, attention_hours, action='A')
        messages.success(self.request, f"Éxito al crear el horario de atención {attention_hours.dia_semana}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class AttentionHoursUpdateView(UpdateView):
    model = HorarioAtencion
    template_name = 'attention/attention_hours/form.html'
    form_class = AttentionHoursForm
    success_url = reverse_lazy('attention:attention_hours_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Actualización de Horarios de Atención'
        context['grabar'] = 'Actualizar Horario de Atención'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        attention_hours = self.object
        save_audit(self.request, attention_hours, action='M')
        messages.success(self.request, f"Éxito al actualizar el horario de atención {attention_hours.dia_semana}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class AttentionHoursDeleteView(DeleteView):
    model = HorarioAtencion
    template_name = 'attention/attention_hours/delete.html'
    success_url = reverse_lazy('attention:attention_hours_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Horario de Atención'
        context['grabar'] = f'¿Está seguro de eliminar el horario de atención {self.object.dia_semana}?'
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        attention_hours = self.get_object()
        save_audit(request, attention_hours, action='E')
        messages.success(request, f"Éxito al eliminar el horario de atención {attention_hours.dia_semana}.")
        return super().delete(request, *args, **kwargs)

class AttentionHoursDetailView(DetailView):
    model = HorarioAtencion
    
    def get(self, request, *args, **kwargs):
        attention_hours = self.get_object()
        data = {
            'id': attention_hours.id,
            'dia_semana': attention_hours.dia_semana,
            'hora_inicio': attention_hours.hora_inicio,
            'hora_fin': attention_hours.hora_fin,
            'Intervalo_desde': attention_hours.Intervalo_desde,
            'Intervalo_hasta': attention_hours.Intervalo_hasta,
            'activo': attention_hours.activo
        }
        return JsonResponse(data)