from django.urls import path
from . import views

urlpatterns = [
    path('', views.maquina_list, name='maquina_list'),
    path('crear/', views.maquina_create, name='maquina_create'),
    path('editar/<int:pk>/', views.maquina_update, name='maquina_update'),
    path('eliminar/<int:pk>/', views.maquina_delete, name='maquina_delete'),
]