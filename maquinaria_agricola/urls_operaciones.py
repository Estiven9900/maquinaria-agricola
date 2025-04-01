from django.urls import path
from . import views

urlpatterns = [
    path('', views.operacion_list, name='operacion_list'),
    path('crear/', views.operacion_create, name='operacion_create'),
    path('editar/<int:pk>/', views.operacion_update, name='operacion_update'),
    path('eliminar/<int:pk>/', views.operacion_delete, name='operacion_delete'),
]