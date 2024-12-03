from django.urls import  path
from servicios_app import views

urlpatterns = [
    path('servicios', views.inicio_vistaServicios, name='servicios'),
    path('registrarServicios/', views.registrarServicios, name='registrarServicios'),
    path("seleccionarServicios/<Id_Servicio>",views.seleccionarServicios,name="seleccionarServicios"),
    path("editarServicios/",views.editarServicios,name="editarServicios"),
    path("borrarServicios/<Id_Servicio>",views.borrarServicios,name="borrarServicios"),
] 