from django.urls import path
from . import views

urlpatterns = [
    path('', views.complemento_list, name='complemento_list'),
    path('crear/', views.complemento_create, name='complemento_create'),
    path('editar/<int:pk>/', views.complemento_update, name='complemento_update'),
    path('eliminar/<int:pk>/', views.complemento_delete, name='complemento_delete'),
]