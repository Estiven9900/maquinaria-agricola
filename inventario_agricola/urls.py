from django.contrib import admin
from django.urls import path, include
from maquinaria_agricola.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('maquinas/', include('maquinaria_agricola.urls')),
    path('complementos/', include('maquinaria_agricola.urls_complementos')),
    path('trabajadores/', include('maquinaria_agricola.urls_trabajadores')),
    path('operaciones/', include('maquinaria_agricola.urls_operaciones')),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación
]