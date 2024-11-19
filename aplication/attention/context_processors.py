from .models import CitaMedica
from .models import Atencion


def cantidad_citas_context(request):
    return {'cantidad_citas': CitaMedica.cantidad_citas()}


def cantidad_atencion_context(request):
    return {'cantidad_examen': Atencion.cantidad_atencion()}