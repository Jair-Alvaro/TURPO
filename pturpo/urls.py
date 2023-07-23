from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', views.home_view, name='reseña'),

    path('listar/', views.list_relaciones, name='list_relaciones'),
    path('crear/', views.create_relacion, name='create_relacion'),
    path('editar/<int:relacion_id>/', views.edit_relacion, name='edit_relacion'),
    path('eliminar/', views.delete_relacion, name='delete_relacion'),

   path('listarO/', views.list_organizaciones, name='list_organizaciones'),
    path('crearO/', views.create_organizacion, name='crear_organizacion'),
    path('editO/<int:organizacion_id>/', views.edit_organizacion, name='edit_organizacion'),
    path('eliminarO/', views.delete_organizacion, name='delete_organizacion'),
]