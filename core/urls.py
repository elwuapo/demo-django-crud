from core.views import AgregarPerro, EliminarPerro, FormularioPerroAgr, FormularioPerroMod, Inicio, ModificarPerro, Perros
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', Inicio, name='Inicio'),
    path('adopta/perros/', Perros, name='Perros'),
    path('adopta/perros/form/agr/', FormularioPerroAgr, name='FormularioPerroAgr'),
    path('adopta/perros/form/mod/<int:nro_chip>/', FormularioPerroMod, name='FormularioPerroMod'),
    path('adopta/perros/form/agr/agregando/', AgregarPerro, name='AgregarPerro'),
    path('adopta/perros/form/mod/modificando/', ModificarPerro, name='ModificarPerro'),
    path('adopta/perros/form/eli/eliminando/<int:nro_chip>/', EliminarPerro, name='EliminarPerro'),
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)