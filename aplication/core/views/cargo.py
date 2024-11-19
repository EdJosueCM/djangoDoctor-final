from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.http import JsonResponse
from django.contrib import messages
from django.db.models import Q
from aplication.core.models import Cargo
from aplication.core.forms.cargo_form import CargoForm
from doctor.utils import save_audit


class CargoListView(ListView):
    template_name = "core/cargo/list.html"
    model = Cargo
    context_object_name = "cargos"
    query = None
    paginate_by = 5

    def get_queryset(self):
        self.query = Q()
        q1 = self.request.GET.get("q")
        if q1 is not None:
            self.query |= Q(nombre__icontains=q1)
            self.query |= Q(descripcion__icontains=q1)
        return self.model.objects.filter(self.query).order_by("nombre")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Gestión de Cargos"
        context["title1"] = "Consulta de Cargos"
        return context


class CargoCreateView(CreateView):
    model = Cargo
    template_name = "core/cargo/form.html"
    form_class = CargoForm
    success_url = reverse_lazy("core:cargo_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title1"] = "Registro de Cargo"
        context["grabar"] = "Grabar Cargo"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        cargo = self.object
        save_audit(self.request, cargo, action="A")
        messages.success(self.request, f"Éxito al crear el cargo {cargo.nombre}.")
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Error al enviar el formulario. Corrige los errores."
        )
        return self.render_to_response(self.get_context_data(form=form))


class CargoUpdateView(UpdateView):
    model = Cargo
    template_name = "core/cargo/form.html"
    form_class = CargoForm
    success_url = reverse_lazy("core:cargo_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title1"] = "Actualización de Cargo"
        context["grabar"] = "Actualizar Cargo"
        context["back_url"] = self.success_url
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        cargo = self.object
        save_audit(self.request, cargo, action="M")
        messages.success(self.request, f"Éxito al actualizar el cargo {cargo.nombre}.")
        return response

    def form_invalid(self, form):
        messages.error(
            self.request, "Error al enviar el formulario. Corrige los errores."
        )
        return self.render_to_response(self.get_context_data(form=form))


class CargoDeleteView(DeleteView):
    model = Cargo
    template_name = "core/cargo/delete.html"
    success_url = reverse_lazy("core:cargo_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context["title1"] = "Eliminar Cargo"
        context["grabar"] = f"¿Está seguro de eliminar el cargo {self.object.nombre}?"
        context["back_url"] = self.success_url
        return context

    def delete(self, request, *args, **kwargs):
        cargo = self.get_object()
        save_audit(request, cargo, action="E")
        messages.success(request, f"Éxito al eliminar el cargo {cargo.nombre}.")
        return super().delete(request, *args, **kwargs)


class CargoDetailView(DetailView):
    model = Cargo

    def get(self, request, *args, **kwargs):
        cargo = self.get_object()
        data = {
            "id": cargo.id,
            "nombre": cargo.nombre,
            "descripcion": cargo.descripcion,
            "activo": cargo.activo,
        }
        return JsonResponse(data)
