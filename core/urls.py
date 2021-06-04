from core.views import AgregarPerro, Deslogeo, EliminarPerro, FormularioPerroAgr, FormularioPerroMod, Inicio, Logeando, ModificarPerro, Perros, SignIn
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

    # Sign In
    path('signin/', SignIn, name='SignIn'),
    path('signin/logeando/', Logeando, name='Logeando'),
    path('signin/deslogeando/', Deslogeo, name='Deslogeo'),
]

urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


"""
from django.contrib.auth.views import LogoutView

path('signin/', SignIn, name='SignIn'),
path('signin/logiando/', Logeando, name='Logeando'),
path('signin/Deslogeando/', Deslogeo, name='Deslogeo'),

path('logout', LogoutView.as_view()),
"""