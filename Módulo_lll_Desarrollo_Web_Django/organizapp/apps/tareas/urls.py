from django.urls import include,path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('usuarios/',include('apps.usuarios.urls')),
    path('',views.inicio,name='inicio'),
    path('agregar/',views.agregar_tarea,name="agregar_tarea"),
    path('listar/',views.listar_tarea,name="listar_tarea"),
    path('login/',views.mi_login,name="mi_login"),
    path('registrate/',views.registrate,name="registrate"),
] 