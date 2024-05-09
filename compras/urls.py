from django.urls import path
from .views import Inicio,CrearOrden
from django.contrib.auth import views as auth_views
from .views import Registro, Dashboard, CrearOrden, CancelarOrden
from . import views

urlpatterns = [
    path('', Inicio.as_view(), name='bienvenida'),
    path('crear-orden/', CrearOrden.as_view(), name='crear-orden'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('iniciar-sesion/', auth_views.LoginView.as_view(template_name='login.html'), name='iniciar-sesion'),
    path('registro/', Registro.as_view(), name='registro'),
    path('cerrar-sesion/', auth_views.LogoutView.as_view(template_name='logout.html'), name='cerrar-sesion'),
    path('cancelar-orden/<int:pk>', CancelarOrden.as_view(), name='cancelar-orden'),
    path('detalles-item/<int:item_id>/', views.DetallesItem, name='detalles-item'),
]
