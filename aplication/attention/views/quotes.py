from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db.models import Q
from aplication.attention.models import CitaMedica
from aplication.attention.forms.quotes import QuoteForm
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from doctor.utils import save_audit
from django.core.mail import send_mail
from datetime import datetime, timedelta
from django.utils import timezone  # Agregamos esto



class QuoteListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "attention/quotes/list.html"
    model = CitaMedica
    context_object_name = 'quotes'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return CitaMedica.objects.filter(
                Q(paciente__nombre__icontains=query) |
                Q(fecha__icontains=query)
            )
        return CitaMedica.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        hoy = timezone.now().date()
        hora_actual = timezone.now().time()
        fecha_limite = hoy + timedelta(days=7)
        
        proximas_citas = CitaMedica.objects.filter(
            Q(fecha=hoy, hora_cita__gte=hora_actual) | Q(fecha__gt=hoy)
        ).order_by('fecha', 'hora_cita')

        context.update({
            'proximas_citas': proximas_citas,
            'fecha_actual': hoy,
            'fecha_limite': fecha_limite,
            'total_citas': proximas_citas.count()
        })

        return context
    
    
class QuoteCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = CitaMedica
    template_name = 'attention/quotes/form.html'
    form_class = QuoteForm
    success_url = reverse_lazy('attention:quote_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Grabar Cita Médica'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        quote = self.object
        save_audit(self.request, quote, action='A')
        messages.success(self.request, f"Éxito al crear la cita médica para {quote.paciente}.")
        
        # Envío de correo al paciente con formato mejorado
        subject = "🏥 Confirmación de tu Cita Médica"
        message = f"""
¡Hola {quote.paciente.nombres}!

Tu cita médica ha sido programada exitosamente.

Detalles de la Cita:
📅 Fecha: {quote.fecha.strftime('%d/%m/%Y')}
⏰ Hora: {quote.hora_cita.strftime('%H:%M')}
📋 Estado: {quote.estado}

Recordatorios importantes:
• Llegar 10 minutos antes a su cita
• Traer su documento de identidad
• En caso de algun problema con su cita comunicarse antes.

¡Gracias por confiar en nuestros servicios médicos!

Atentamente,
El equipo médico
------------------------------------------
Este es un correo automático, por favor no responder.
"""
        recipient_email = quote.paciente.email
        send_mail(
            subject,
            message,
            from_email=None,
            recipient_list=[recipient_email],
            fail_silently=False,
        )

        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class QuoteUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = CitaMedica
    template_name = 'attention/quotes/form.html'
    form_class = QuoteForm
    success_url = reverse_lazy('attention:quote_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Cita Médica'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        quote = self.object
        save_audit(self.request, quote, action='M')
        messages.success(self.request, f"Éxito al modificar la cita médica para {quote.paciente}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al modificar el formulario. Corrige los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class QuoteDeleteView(DeleteView, DeleteViewMixin, LoginRequiredMixin):
    model = CitaMedica
    # template_name = 'attention/quotes/delete.html'
    success_url = reverse_lazy('attention:quote_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request, "Cita médica eliminada con éxito.")
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Esta cita médica no se puede eliminar porque está en uso.")
            return redirect(self.success_url)

class QuoteDetailView(LoginRequiredMixin, DetailView):
    model = CitaMedica

    def get(self, request, *args, **kwargs):
        quote = self.get_object()
        data = {
            'id': quote.id,
            'paciente': quote.paciente.nombres,
            'fecha': quote.fecha.strftime('%Y-%m-%d'),
            'hora_cita': quote.hora_cita.strftime('%H:%M'),
            'estado': quote.estado,
        }
        return JsonResponse(data)