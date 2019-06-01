from django.urls import include,path
from . import views
urlpatterns = [
    path('usuarios/',include('apps.usuarios.urls')),
    path('',views.inicio,name='inicio'),
    path('agregar/',views.agregar_tarea,name="agregar_tarea"),
]
