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
    path('avisos/crear_aviso',views.avisos,name='crear_aviso')
]

