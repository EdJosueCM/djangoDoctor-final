from django.urls import reverse_lazy
from aplication.core.forms.employees import EmployeeForm
from aplication.core.models import Empleado
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from doctor.utils import save_audit

class EmployeeListView(ListView):
    template_name = "core/employees/list.html"
    model = Empleado
    context_object_name = 'empleados'
    query = None
    paginate_by = 5
    
    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get('q')  # ver
        if q1 is not None:
            self.query.add(Q(nombres__icontains=q1), Q.OR)
            self.query.add(Q(apellidos__icontains=q1), Q.OR)
            self.query.add(Q(cedula__icontains=q1), Q.OR)
            self.query.add(Q(cargo__nombre__icontains=q1), Q.OR) 
        return self.model.objects.filter(self.query).order_by('apellidos')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Medical"
        context['title1'] = "Consulta de Empleados"
        return context

class EmployeeCreateView(CreateView):
    model = Empleado
    template_name = 'core/employees/form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('core:employee_list')
    # permission_required = 'add_supplier' # en PermissionMixn se verfica si un grupo tiene el permiso

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Registro de Empleados'
        context['grabar'] = 'Grabar Empleado'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        # print("entro al form_valid")
        response = super().form_valid(form)
        employee = self.object
        save_audit(self.request, employee, action='A')
        messages.success(self.request, f"Éxito al crear al empleado {employee.nombre_completo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class EmployeeUpdateView(UpdateView):
    model = Empleado
    template_name = 'core/employees/form.html'
    form_class = EmployeeForm
    success_url = reverse_lazy('core:employee_list')
    # permission_required = 'change_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Actualización de Empleados'
        context['grabar'] = 'Actualizar Empleado'
        context['back_url'] = self.success_url
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        employee = self.object
        save_audit(self.request, employee, action='M')
        messages.success(self.request, f"Éxito al actualizar al empleado {employee.nombre_completo}.")
        return response
    
    def form_invalid(self, form):
        messages.error(self.request, "Error al enviar el formulario. Corrige los errores.")
        print(form.errors)
        return self.render_to_response(self.get_context_data(form=form))

class EmployeeDeleteView(DeleteView):
    model = Empleado
    template_name = 'core/employee/delete.html'
    success_url = reverse_lazy('core:employee_list')
    # permission_required = 'delete_supplier'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Empleado'
        context['descripcion'] = f'¿Está seguro que desea eliminar el empleado: {self.name}?'
        context['back_url'] = self.success_url
        return context
    
    def delete(self, request, *args, **kwargs):
        employee = self.get_object()
        employee.activo = False
        employee.save()
        save_audit(self.request, employee, action='D')
        messages.success(self.request, f"Éxito al eliminar al empleado {employee.nombre_completo}.")
        return JsonResponse({'url': self.success_url})
    
class EmployeeDetailView(DetailView):
    model = Empleado
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {   
            'id': self.object.id,
            'nombres': self.object.nombres,
            'apellidos': self.object.apellidos,
            'cedula': self.object.cedula,
            'fecha_nacimiento': self.object.fecha_nacimiento,
            'cargo': str(self.object.cargo),  # Convert cargo to string
            'sueldo': self.object.sueldo,
            'direccion': self.object.direccion,
            'latitud': self.object.latitud,
            'longitud': self.object.longitud,
            'foto': self.object.foto.url,
            'activo': self.object.activo,
        }
        return JsonResponse(data)