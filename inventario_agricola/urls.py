from django.contrib import admin
from django.urls import path, include
from maquinaria_agricola.views import home  # Importa la vista home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Ruta para la página de inicio
    path('maquinas/', include('maquinaria_agricola.urls')),  # Máquinas
    path('complementos/', include('maquinaria_agricola.urls_complementos')),  # Complementos
    path('trabajadores/', include('maquinaria_agricola.urls_trabajadores')),  # Trabajadores
    path('operaciones/', include('maquinaria_agricola.urls_operaciones')),  # Operaciones
]