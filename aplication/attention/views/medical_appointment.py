from django.urls import reverse_lazy
from aplication.attention.forms.medical_appointment import MedicalAppointmentForm
from aplication.attention.models import CitaMedica
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class MedicalAppointmentListView(ListView):
    template_name = "attention/medical_appointment/list.html"
    model = CitaMedica
    context_object_name = 'Citas_Medicas'
    query = None
    paginate_by = 5
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')
        if q1 is not None: 
            self.query |= Q(paciente__icontains=q1) 
            self.query |= Q(fecha__icontains=q1)  
        return self.model.objects.filter(self.query).order_by('fecha')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Citas Médicas"
        return context
    

class MedicalAppointmentCreateView(CreateView):
    model = CitaMedica
    template_name = 'attention/medical_appointment/form.html'
    form_class = MedicalAppointmentForm
    success_url = reverse_lazy('attention:medical_appointment_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Citas Médicas'
        context['grabar'] = 'Grabar Cita Médica'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        medical_appointment = self.object
        save_audit(self.request, medical_appointment, action='A')
        messages.success(self.request, f"Éxito al crear la cita médica para {medical_appointment.paciente}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))
    
class MedicalAppointmentUpdateView(UpdateView):
    model = CitaMedica
    template_name = 'attention/medical_appointment/form.html'
    form_class = MedicalAppointmentForm
    success_url = reverse_lazy('attention:medical_appointment_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Actualización de Citas Médicas'
        context['grabar'] = 'Actualizar Cita Médica'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        medical_appointment = self.object
        save_audit(self.request, medical_appointment, action='M')
        messages.success(self.request, f"Éxito al actualizar la cita médica para {medical_appointment.paciente}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class MedicalAppointmentDeleteView(DeleteView):
    model = CitaMedica
    template_name = 'attention/medical_appointment/delete.html'
    success_url = reverse_lazy('attention:medical_appointment_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Cita Médica'
        context['grabar'] = f'¿Está seguro de eliminar la cita médica para {self.object.paciente}?'
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        medical_appointment = self.get_object()
        save_audit(request, medical_appointment, action='E')
        messages.success(request, f"Éxito al eliminar la cita médica para {medical_appointment.paciente}.")
        return super().delete(request, *args, **kwargs)

class MedicalAppointmentDetailView(DetailView):
    model = CitaMedica
    
    def get(self, request, *args, **kwargs):
        medical_appointment = self.get_object()
        data = {
            'id': medical_appointment.id,
            'paciente': str(medical_appointment.paciente),
            'fecha': medical_appointment.fecha,
            'hora_cita': medical_appointment.hora_cita,
            'estado': medical_appointment.estado
        }
        return JsonResponse(data)