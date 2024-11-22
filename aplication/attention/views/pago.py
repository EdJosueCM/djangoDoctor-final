from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from django.http import JsonResponse
from django.forms import modelformset_factory
from aplication.attention.models import CostosAtencion, CostoAtencionDetalle, ServiciosAdicionales, Atencion
from aplication.attention.forms.PagoForm import CostosAtencionForm, CostoAtencionDetalleForm

class CostosAtencionListView(LoginRequiredMixin, ListView):
    model = CostosAtencion
    template_name = 'attention/costos/list.html'
    context_object_name = 'costos'
    paginate_by = 5
    
    def get_queryset(self):
        return CostosAtencion.objects.filter(activo=True).select_related('atencion')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Costos de Atención'
        return context

class CostosAtencionCreateView(LoginRequiredMixin, CreateView):
    model = CostosAtencion
    form_class = CostosAtencionForm
    template_name = 'attention/costos/form.html'
    success_url = reverse_lazy('attention:costos_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar Nuevo Costo de Atención'
        if self.request.POST:
            context['detalles_formset'] = self.get_detalles_formset(self.request.POST)
        else:
            context['detalles_formset'] = self.get_detalles_formset()
        return context
    
    def get_detalles_formset(self, data=None):
        DetallesFormSet = modelformset_factory(
            CostoAtencionDetalle,
            form=CostoAtencionDetalleForm,
            extra=1,
            can_delete=True
        )
        return DetallesFormSet(data=data, queryset=CostoAtencionDetalle.objects.none())
    
    @transaction.atomic
    def form_valid(self, form):
        context = self.get_context_data()
        detalles_formset = context['detalles_formset']
        
        if detalles_formset.is_valid():
            try:
                self.object = form.save()
                detalles = detalles_formset.save(commit=False)
                
                # Calcular el total de los costos
                total = 0
                for detalle in detalles:
                    detalle.costo_atencion = self.object
                    detalle.save()
                    total += detalle.costo_servicio
                
                # Actualizar el total en el modelo principal
                self.object.total = total
                self.object.save()
                
                if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': True,
                        'message': 'Costo de atención registrado exitosamente.'
                    })
                
                messages.success(self.request, 'Costo de atención registrado exitosamente.')
                return redirect(self.success_url)
            
            except Exception as e:
                if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                    return JsonResponse({
                        'success': False,
                        'error': str(e)
                    }, status=400)
                raise
        else:
            if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                errors = {}
                if form.errors:
                    errors.update(form.errors)
                if detalles_formset.errors:
                    errors.update({'detalles': detalles_formset.errors})
                return JsonResponse({
                    'success': False,
                    'error': 'Por favor, corrija los errores en el formulario.',
                    'errors': errors
                }, status=400)
            return self.form_invalid(form)
    
    def form_invalid(self, form):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': False,
                'error': 'Por favor, corrija los errores en el formulario.',
                'errors': form.errors
            }, status=400)
        return super().form_invalid(form)

# Vista auxiliar para obtener el costo del servicio seleccionado
def get_servicio_costo(request):
    servicio_id = request.GET.get('servicio_id')
    try:
        servicio = ServiciosAdicionales.objects.get(id=servicio_id)
        return JsonResponse({
            'success': True,
            'costo': float(servicio.costo_servicio)
        })
    except ServiciosAdicionales.DoesNotExist:
        return JsonResponse({
            'success': False,
            'error': 'Servicio no encontrado'
        }, status=404)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'error': str(e)
        }, status=500)

class CostosAtencionUpdateView(LoginRequiredMixin, UpdateView):
    model = CostosAtencion
    form_class = CostosAtencionForm
    template_name = 'attention/costos/form.html'
    success_url = reverse_lazy('costos_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Costo de Atención'
        if self.request.POST:
            context['detalles_formset'] = self.get_detalles_formset(self.request.POST)
        else:
            context['detalles_formset'] = self.get_detalles_formset()
        return context
    
    def get_detalles_formset(self, data=None):
        DetallesFormSet = modelformset_factory(
            CostoAtencionDetalle,
            form=CostoAtencionDetalleForm,
            extra=1,
            can_delete=True
        )
        queryset = CostoAtencionDetalle.objects.filter(costo_atencion=self.object)
        return DetallesFormSet(data=data, queryset=queryset)
    
    @transaction.atomic
    def form_valid(self, form):
        context = self.get_context_data()
        detalles_formset = context['detalles_formset']
        
        if detalles_formset.is_valid():
            self.object = form.save()
            detalles = detalles_formset.save(commit=False)
            
            # Eliminar detalles marcados para eliminación
            for obj in detalles_formset.deleted_objects:
                obj.delete()
            
            # Calcular el total de los costos
            total = 0
            for detalle in detalles:
                detalle.costo_atencion = self.object
                detalle.save()
                total += detalle.costo_servicio
            
            # Actualizar el total en el modelo principal
            self.object.total = total
            self.object.save()
            
            messages.success(self.request, 'Costo de atención actualizado exitosamente.')
            return redirect(self.success_url)
        else:
            return self.form_invalid(form)

class CostosAtencionDeleteView(LoginRequiredMixin, DeleteView):
    model = CostosAtencion
    template_name = 'attention/costos/delete.html'
    success_url = reverse_lazy('attention:costos_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['title1'] = 'Eliminar Costo de Atención'
        context['grabar'] = f'¿Está seguro de eliminar el costo de atención con ID {self.object.id}?'
        context['back_url'] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        costos_atencion = self.get_object()
        costos_atencion.activo = False
        costos_atencion.save()
        messages.success(request, f"Éxito al eliminar el costo de atención con ID {costos_atencion.id}.")
        return redirect(self.success_url)

# Vista auxiliar para obtener el costo del servicio seleccionado
def get_servicio_costo(request):
    servicio_id = request.GET.get('servicio_id')
    try:
        servicio = ServiciosAdicionales.objects.get(id=servicio_id)
        return JsonResponse({
            'costo': float(servicio.costo_servicio)
        })
    except ServiciosAdicionales.DoesNotExist:
        return JsonResponse({'error': 'Servicio no encontrado'}, status=404)