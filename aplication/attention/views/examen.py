from datetime import timezone
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.db.models.deletion import ProtectedError
from django.shortcuts import redirect
from django.http import JsonResponse
from django.db.models import Q
# Importa los modelos necesarios
from aplication.attention.models import Examen  
from aplication.attention.forms.ExamenForm import ExamenForm  # Asumo que crearás este formulario
# Importa utilidades si las tienes
from doctor.mixins import CreateViewMixin, DeleteViewMixin, ListViewMixin, UpdateViewMixin
from doctor.utils import save_audit

class ExamenListView(LoginRequiredMixin, ListViewMixin, ListView):
    template_name = "attention/examenes/list.html"
    model = Examen
    context_object_name = 'examenes'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Examen.objects.filter(
                Q(tipo_examen__icontains=query) |
                Q(estado__icontains=query) |
                Q(atencion__paciente__nombre__icontains=query)
            )
        return Examen.objects.all()

class ExamenCreateView(LoginRequiredMixin, CreateViewMixin, CreateView):
    model = Examen
    template_name = 'attention/examenes/form.html'
    form_class = ExamenForm
    success_url = reverse_lazy('attention:examen_list')

    def form_valid(self, form):
        if hasattr(self.request.user, 'doctor'):
            form.instance.doctor = self.request.user.doctor
        
        # Si se subió un archivo PDF, marca el examen como completado
        if form.cleaned_data.get('archivo_resultado'):
            form.instance.estado = 'COMPLETADO'
            form.instance.fecha_realizacion = timezone.now()

        response = super().form_valid(form)
        examen = self.object
        save_audit(self.request, examen, action='A')
        messages.success(self.request, f"Éxito al crear el examen de {examen.get_tipo_examen_display()}.")
        return response

class ExamenUpdateView(LoginRequiredMixin, UpdateViewMixin, UpdateView):
    model = Examen
    template_name = 'attention/examenes/form.html'
    form_class = ExamenForm
    success_url = reverse_lazy('attention:examen_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['grabar'] = 'Actualizar Examen'
        context['back_url'] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        examen = self.object
        save_audit(self.request, examen, action='M')
        messages.success(self.request, f"Éxito al modificar el examen de {examen.get_tipo_examen_display()}.")
        return response

    def form_invalid(self, form):
        messages.error(self.request, "Error al modificar el examen. Por favor, corrija los errores.")
        return self.render_to_response(self.get_context_data(form=form))

class ExamenDeleteView(DeleteView, DeleteViewMixin, LoginRequiredMixin):
    model = Examen
    template_name = 'attention/examenes/delete.html'
    success_url = reverse_lazy('attention:examen_list')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        try:
            self.object.delete()
            messages.success(request, "Examen eliminado con éxito.")
            return redirect(self.success_url)
        except ProtectedError:
            messages.error(request, "Este examen no se puede eliminar porque está en uso.")
            return redirect(self.success_url)

class ExamenDetailView(LoginRequiredMixin, DetailView):
    model = Examen
    template_name = 'attention/examenes/detail_modal.html'  # Opcional: Vista de detalle HTML

    def get(self, request, *args, **kwargs):
        examen = self.get_object()
        data = {
            'id': examen.id,
            'tipo_examen': examen.get_tipo_examen_display(),
            'estado': examen.get_estado_display(),
            'fecha_solicitud': examen.fecha_solicitud.strftime('%Y-%m-%d %H:%M'),
            'doctor': examen.doctor.nombre if examen.doctor else 'No asignado',
            'archivo_resultado': examen.archivo_resultado.url if examen.archivo_resultado else None
        }
        return JsonResponse(data)

# Vista adicional para subir resultados de examen
# class ExamenUploadResultadoView(LoginRequiredMixin, UpdateView):
#     model = Examen
#     template_name = 'attention/examenes/upload_resultado.html'
#     fields = ['archivo_resultado', 'observaciones_doctor', 'estado']
#     success_url = reverse_lazy('attention:examen_list')

#     def form_valid(self, form):
#         # Marcar como completado automáticamente
#         form.instance.estado = 'completado'
#         response = super().form_valid(form)
#         messages.success(self.request, "Resultado de examen subido con éxito.")
#         return response