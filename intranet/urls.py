from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('',views.index, name='index'),
    path('registro/',views.registro,name='formulario'),
    path('registro/crear',views.crear,name='crear'),
    path('entrar',views.entrar,name="entrar"),
    path('cerrar_session',views.cerrar_session,name="cerrar_session"),
    path('entrar/iniciar',views.entrar_iniciar,name="iniciar"),
    path('avisos',views.avisos,name='avisos'),
    path('avisos/crear_aviso',views.crear_aviso,name='crear_aviso'),
    path('trabajo',views.trabajo,name='trabajo'),
    path('transporte',views.transporte,name='transporte'),
    path('documentacion',views.documentacion,name='documentacion'),
    path('conocer',views.conocer,name='conocer'),
    path('educacion',views.educacion,name='educacion'),
    path('salud',views.salud,name='salud'),
    path('vivienda',views.vivienda,name='vivienda'),
]

