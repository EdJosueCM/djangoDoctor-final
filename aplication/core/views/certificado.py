# from django.urls import reverse_lazy
# from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
# from django.contrib import messages
# from django.db.models import Q
# from django.http import JsonResponse
# from django.template.loader import render_to_string
# from weasyprint import HTML
# from aplication.core.models import Certificado
# from aplication.core.forms.CertificadoForm import CertificadoForm
# from doctor.utils import save_audit  # Asegúrate de tener la función de auditoría

# import tempfile

# class CertificadoListView(ListView):
#     model = Certificado
#     template_name = 'core/certificados/list.html'
#     context_object_name = 'certificados'
#     paginate_by = 5
#     query = None

#     def get_queryset(self):
#         self.query = Q()
#         q1 = self.request.GET.get('q')  # Búsqueda de nombre de paciente, doctor o tipo
#         if q1:
#             self.query |= Q(paciente__nombre_completo__icontains=q1)
#             self.query |= Q(doctor__nombre_completo__icontains=q1)
#             self.query |= Q(tipo__icontains=q1)
#         return self.model.objects.filter(self.query).order_by('fecha_emision')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title1'] = 'Consulta de Certificados Médicos'
#         return context

# class CertificadoCreateView(CreateView):
#     model = Certificado
#     template_name = 'core/certificados/form.html'
#     form_class = CertificadoForm  # Asegúrate de crear este formulario
#     success_url = reverse_lazy('core:certificado_list')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['title1'] = 'Registro de Certificado Médico'
#         context['grabar'] = 'Grabar Certificado Médico'
#         context['back_url'] = self.success_url
#         return context

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         certificado = self.object
        
#         # Guardar la auditoría
#         save_audit(self.request, certificado, action='A')

#         # Mensaje de éxito
#         messages.success(self.request, f"Éxito al crear el certificado médico para {certificado.paciente.nombre_completo}.")

#         # Generar el PDF del certificado
#         self.generar_certificado_pdf(certificado)

#         return response

#     def form_invalid(self, form):
#         messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
#         return self.render_to_response(self.get_context_data(form=form))

#     def generar_certificado_pdf(self, certificado):
#         # Genera el PDF del certificado
#         context = {
#             'paciente': certificado.paciente,
#             'doctor': certificado.doctor,
#             'tipo': certificado.tipo,
#             'fecha_emision': certificado.fecha_emision,
#             'observaciones': certificado.observaciones,
#         }

#         # Renderiza la plantilla HTML del certificado
#         html_string = render_to_string('certificados/certificado_pdf.html', context)
#         html = HTML(string=html_string)
#         pdf = html.write_pdf()

#         # Guardar el archivo PDF en un archivo temporal
#         temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
#         temp_file.write(pdf)
#         temp_file.close()

#         # Guardar la ruta del archivo PDF en el modelo
#         certificado.archivo_pdf = temp_file.name
#         certificado.save()

# class CertificadoUpdateView(UpdateView):
#     model = Certificado
#     template_name = 'core/certificados/form.html'
#     form_class = CertificadoForm
#     success_url = reverse_lazy('core:certificado_list')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title1'] = 'Actualización de Certificado Médico'
#         context['grabar'] = 'Actualizar Certificado Médico'
#         context['back_url'] = self.success_url
#         return context

#     def form_valid(self, form):
#         response = super().form_valid(form)
#         certificado = self.object
        
#         # Guardar la auditoría
#         save_audit(self.request, certificado, action='M')

#         # Mensaje de éxito
#         messages.success(self.request, f"Éxito al actualizar el certificado médico para {certificado.paciente.nombre_completo}.")
        
#         return response

#     def form_invalid(self, form):
#         messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
#         return self.render_to_response(self.get_context_data(form=form))

# class CertificadoDeleteView(DeleteView):
#     model = Certificado
#     template_name = 'core/certificados/delete.html'
#     success_url = reverse_lazy('core:certificado_list')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title1'] = 'Eliminar Certificado Médico'
#         context['grabar'] = f'¿Está seguro de eliminar el certificado médico para {self.object.paciente.nombre_completo}?'
#         context['back_url'] = self.success_url
#         return context

#     def delete(self, request, *args, **kwargs):
#         certificado = self.get_object()
        
#         # Guardar la auditoría
#         save_audit(request, certificado, action='E')

#         # Mensaje de éxito
#         messages.success(request, f"Éxito al eliminar el certificado médico para {certificado.paciente.nombre_completo}.")
        
#         return super().delete(request, *args, **kwargs)

# class CertificadoDetailView(DetailView):
#     model = Certificado

#     def get(self, request, *args, **kwargs):
#         certificado = self.get_object()
#         data = {
#             'id': certificado.id,
#             'paciente': certificado.paciente.nombre_completo,
#             'doctor': certificado.doctor.nombre_completo,
#             'tipo': certificado.tipo,
#             'fecha_emision': certificado.fecha_emision,
#             'observaciones': certificado.observaciones,
#         }
#         return JsonResponse(data)
