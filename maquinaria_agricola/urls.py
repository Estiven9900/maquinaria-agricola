from django.urls import path
from . import views

urlpatterns = [
    # Máquinas
    path('maquinas/', views.maquina_list, name='maquina_list'),
    path('maquinas/crear/', views.maquina_create, name='maquina_create'),
    path('maquinas/editar/<int:pk>/', views.maquina_update, name='maquina_update'),
    path('maquinas/eliminar/<int:pk>/', views.maquina_delete, name='maquina_delete'),

    # Complementos
    path('complementos/', views.complemento_list, name='complemento_list'),
    path('complementos/crear/', views.complemento_create, name='complemento_create'),
    path('complementos/editar/<int:pk>/', views.complemento_update, name='complemento_update'),
    path('complementos/eliminar/<int:pk>/', views.complemento_delete, name='complemento_delete'),

    # Trabajadores
    path('trabajadores/', views.trabajador_list, name='trabajador_list'),
    path('trabajadores/crear/', views.trabajador_create, name='trabajador_create'),
    path('trabajadores/editar/<int:pk>/', views.trabajador_update, name='trabajador_update'),
    path('trabajadores/eliminar/<int:pk>/', views.trabajador_delete, name='trabajador_delete'),

    # Operaciones
    path('operaciones/', views.operacion_list, name='operacion_list'),
    path('operaciones/crear/', views.operacion_create, name='operacion_create'),
    path('operaciones/editar/<int:pk>/', views.operacion_update, name='operacion_update'),
    path('operaciones/eliminar/<int:pk>/', views.operacion_delete, name='operacion_delete'),
]