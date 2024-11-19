from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.core.models import MarcaMedicamento
from aplication.core.forms.MarcaMedicamentoForm import MarcaMedicamentoForm

class MarcaMedicamentoListView(ListView):
    model = MarcaMedicamento
    template_name = "core/marca/list.html"
    context_object_name = "marcas_medicamento"
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
        context["title"] = "Marcas de Medicamento"
        context["title1"] = "Consulta de Marcas de Medicamentos"
        return context

class MarcaMedicamentoCreateView(CreateView):
    model = MarcaMedicamento
    template_name = "core/marca/form.html"
    form_class = MarcaMedicamentoForm
    success_url = reverse_lazy("core:marca_medicamento_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Registro de Marca de Medicamento"
        context["grabar"] = "Grabar Marca de Medicamento"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request, f"Éxito al crear la marca de medicamento {self.object.nombre}."
        )
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Error al enviar el formulario. Corrige los errores."
        )
        return self.render_to_response(self.get_context_data(form=form))

class MarcaMedicamentoUpdateView(UpdateView):
    model = MarcaMedicamento
    template_name = "core/marca/form.html"
    form_class = MarcaMedicamentoForm
    success_url = reverse_lazy("core:marca_medicamento_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Actualización de Marca de Medicamento"
        context["grabar"] = "Actualizar Marca de Medicamento"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            f"Éxito al modificar la marca de medicamento {self.object.nombre}.",
        )
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Error al enviar el formulario. Corrige los errores."
        )
        return self.render_to_response(self.get_context_data(form=form))

class MarcaMedicamentoDeleteView(DeleteView):
    model = MarcaMedicamento
    success_url = reverse_lazy("core:marca_medicamento_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title1"] = "Eliminar Marca de Medicamento"
        context["description"] = (
            f"¿Está seguro de eliminar la marca de medicamento: {self.object.nombre}?"
        )
        context["back_url"] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        messages.success(
            self.request,
            f"Éxito al eliminar la marca de medicamento {self.object.nombre}.",
        )
        return super().delete(request, *args, **kwargs)

class MarcaMedicamentoDetailView(DetailView):
    model = MarcaMedicamento

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        data = {
            "id": self.object.id,
            "nombre": self.object.nombre,
            "descripcion": self.object.descripcion,
            "activo": self.object.activo,
        }
        return JsonResponse(data)
