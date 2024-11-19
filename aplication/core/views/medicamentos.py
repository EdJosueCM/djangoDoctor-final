from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.core.forms.MedicamentoForm import MedicamentoForm
from aplication.core.models import Medicamento


class MedicamentoListView(ListView):
    model = Medicamento
    template_name = "core/medicamento/list.html"
    context_object_name = "medicamentos"
    paginate_by = 5  

    def get_queryset(self):
        query = Q()
        search_query = self.request.GET.get("q")
        if search_query:
            query.add(Q(nombre__icontains=search_query), Q.OR)
            query.add(Q(descripcion__icontains=search_query), Q.OR)
        return self.model.objects.filter(query).order_by("nombre")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Farmacia"
        context["title1"] = "Consulta de Medicamentos"
        return context


class MedicamentoCreateView(CreateView):
    model = Medicamento
    template_name = "core/medicamento/form.html"
    form_class = MedicamentoForm
    success_url = reverse_lazy("core:medicamento_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Registro de Medicamentos"
        context["grabar"] = "Grabar Medicamento"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        medicamento = self.object
        messages.success(
            self.request, f"Éxito al crear el medicamento {medicamento.nombre}."
        )
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Error al enviar el formulario. Corrige los errores."
        )
        return self.render_to_response(self.get_context_data(form=form))


class MedicamentoUpdateView(UpdateView):
    model = Medicamento
    template_name = "core/medicamento/form.html"
    form_class = MedicamentoForm
    success_url = reverse_lazy("core:medicamento_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Actualización de Medicamentos"
        context["grabar"] = "Actualizar Medicamento"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        medicamento = self.object
        messages.success(
            self.request, f"Éxito al modificar el medicamento {medicamento.nombre}."
        )
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Error al enviar el formulario. Corrige los errores."
        )
        return self.render_to_response(self.get_context_data(form=form))


class MedicamentoDeleteView(DeleteView):
    model = Medicamento
    success_url = reverse_lazy("core:medicamento_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Eliminar Medicamento"
        context["description"] = (
            f"¿Está seguro de eliminar el medicamento: {self.object.nombre}?"
        )
        context["back_url"] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_message = f"Éxito al eliminar el medicamento {self.object.nombre}."
        messages.success(self.request, success_message)
        return super().delete(request, *args, **kwargs)


class MedicamentoDetailView(DetailView):
    model = Medicamento

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {
            "id": self.object.id,
            "nombre": self.object.nombre,
            "tipo": self.object.tipo.nombre,  # Asegúrate de que `TipoMedicamento` tenga un campo `nombre`
            "marca_medicamento": (
                self.object.marca_medicamento.nombre
                if self.object.marca_medicamento
                else None
            ),
            "descripcion": self.object.descripcion,
            "concentracion": self.object.concentracion,
            "cantidad": self.object.cantidad,
            "precio": float(self.object.precio),
            "comercial": self.object.comercial,
            "foto": self.object.foto.url if self.object.foto else None,
            "activo": self.object.activo,
        }
        return JsonResponse(data)
