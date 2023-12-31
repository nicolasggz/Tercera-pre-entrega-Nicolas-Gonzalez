
from django.urls import path
from inicio import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('propietarios/', views.propietarios, name='propietarios'),
    path('mascotas/', views.mascotas, name='mascotas'),
    path('veterinarios/', views.veterinarios, name='veterinarios'),
    path('veterinario/agregar/', views.agregar_veterinario, name='agregar_veterinario'),
    path('propietario/agregar/', views.agregar_propietario, name='agregar_propietario'),
    path('mascota/agregar/', views.agregar_mascota, name='agregar_mascota'),
    path('buscar/', views.buscar, name='buscar'),
    ]

