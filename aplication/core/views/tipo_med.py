from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.core.models import TipoMedicamento
from aplication.core.forms.tipo_med import TipoMedicamentoForm


class TipoMedicamentoListView(ListView):
    model = TipoMedicamento
    template_name = "core/tipomedicamento/list.html"
    context_object_name = "tipos_medicamento"
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
        context["title"] = "Tipos de Medicamento"
        context["title1"] = "Consulta de Tipos de Medicamentos"
        return context


class TipoMedicamentoCreateView(CreateView):
    model = TipoMedicamento
    template_name = "core/tipomedicamento/form.html"
    form_class = TipoMedicamentoForm
    success_url = reverse_lazy("core:medicamento_type_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Registro de Tipo de Medicamento"
        context["grabar"] = "Grabar Tipo de Medicamento"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f"Éxito al crear el tipo de medicamento {self.object.nombre}."
        )
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Error al enviar el formulario. Corrige los errores."
        )
        return self.render_to_response(self.get_context_data(form=form))


class TipoMedicamentoUpdateView(UpdateView):
    model = TipoMedicamento
    template_name = "core/tipomedicamento/form.html"
    form_class = TipoMedicamentoForm
    success_url = reverse_lazy("core:tipomedicamento_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Actualización de Tipo de Medicamento"
        context["grabar"] = "Actualizar Tipo de Medicamento"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Éxito al modificar el tipo de medicamento {self.object.nombre}.",
        )
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Error al enviar el formulario. Corrige los errores."
        )
        return self.render_to_response(self.get_context_data(form=form))


class TipoMedicamentoDeleteView(DeleteView):
    model = TipoMedicamento
    success_url = reverse_lazy("core:tipomedicamento_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Eliminar Tipo de Medicamento"
        context["description"] = (
            f"¿Está seguro de eliminar el tipo de medicamento: {self.object.nombre}?"
        )
        context["back_url"] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(
            self.request,
            f"Éxito al eliminar el tipo de medicamento {self.object.nombre}.",
        )
        return super().delete(request, *args, **kwargs)


class TipoMedicamentoDetailView(DetailView):
    model = TipoMedicamento

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {
            "id": self.object.id,
            "nombre": self.object.nombre,
            "descripcion": self.object.descripcion,
            "activo": self.object.activo,
        }
        return JsonResponse(data)
