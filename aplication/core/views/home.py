from django.views.generic import TemplateView

from aplication.core.models import Paciente
from aplication.attention.models import CitaMedica, Atencion

class HomeTemplateView(TemplateView):
    template_name = 'core/home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {"title1": "SaludSync", "title2": "Sistema Medico"}
        context["can_paci"] = Paciente.cantidad_pacientes()
        context["can_citas"] = CitaMedica.cantidad_citas()
        context["can_atencion"] = Atencion.cantidad_atencion()
        print(context["can_paci"])
        print(context["can_citas"])
        return context 