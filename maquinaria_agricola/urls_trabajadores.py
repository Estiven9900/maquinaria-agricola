from django.urls import path
from . import views

urlpatterns = [
    path('', views.trabajador_list, name='trabajador_list'),
    path('crear/', views.trabajador_create, name='trabajador_create'),
    path('editar/<int:pk>/', views.trabajador_update, name='trabajador_update'),
    path('eliminar/<int:pk>/', views.trabajador_delete, name='trabajador_delete'),
]