from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('maquinaria_agricola.urls')),  # Incluye todas las URLs de la app
]