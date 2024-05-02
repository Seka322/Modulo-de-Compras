from django.urls import path
from .views import Inicio,CrearOrden

urlpatterns = [
    path('', Inicio.as_view(), name='bienvenida'),
    path('crear-orden/', CrearOrden.as_view(), name='crear-orden'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
]
