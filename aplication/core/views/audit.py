from django.urls import reverse_lazy
from aplication.core.forms.audit import AuditUserForm
from aplication.core.models import AuditUser
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class AuditUserListView(ListView):
    template_name = "core/audit/list.html"
    model = AuditUser
    context_object_name = 'Audit_Users'
    query = None
    paginate_by = 5
        
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')
        if q1 is not None:
            self.query |= Q(usuario__username__icontains=q1)
            self.query |= Q(tabla__icontains=q1)  # Corrected field name
        return self.model.objects.filter(self.query).order_by('fecha', 'hora')

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Audit"
        context['title1'] = "Consulta de Auditoría de Usuarios"
        return context
    

class AuditUserDetailView(DetailView):
    model = AuditUser
    
    def get(self, request, *args, **kwargs):
        audit_user = self.get_object()
        data = {
            'id': audit_user.id,
            'usuario': audit_user.usuario.username,
            'tabla': audit_user.tabla,
            'registroid': audit_user.registroid,
            'accion': audit_user.accion,
            'fecha': audit_user.fecha,
            'hora': audit_user.hora,
            'estacion': audit_user.estacion
        }
        return JsonResponse(data)