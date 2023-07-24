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

    path('listarC/', views.list_contactos, name='list_contactos'),
    path('crearC/', views.create_contacto, name='crear_contacto'),
    path('editC/<int:contacto_id>/', views.edit_contacto, name='edit_contacto'),
    path('eliminarC/', views.delete_contacto, name='delete_contacto'), 

    path('listarCategoria/', views.list_categorias, name='list_categorias'),
    path('crearCategoria/', views.create_categoria, name='create_categoria'),
    path('editCategoria/<int:categoria_id>/', views.edit_categoria, name='edit_categoria'),
    path('eliminarCategoria/', views.delete_categoria, name='delete_categoria'),

    path('listarproyectos/', views.list_proyectos, name='list_proyectos'),
    path('crearproyecto/', views.create_proyecto, name='crear_proyecto'),
    path('editarproyecto/<int:proyecto_id>/', views.edit_proyecto, name='edit_proyecto'),
    path('eliminarproyecto/', views.delete_proyecto, name='delete_proyecto'),

    path('listartareas/', views.list_tareas, name='list_tareas'),
    path('creartarea/', views.create_tarea, name='create_tarea'),
    path('editartarea/<int:tarea_id>/', views.edit_tarea, name='edit_tarea'),
    path('eliminartarea/', views.delete_tarea, name='delete_tarea'),

    path('listartipo_recursos/', views.list_tipo_recursos, name='list_tipo_recursos'),
    path('creartipo_recurso/', views.create_tipo_recurso, name='create_tipo_recurso'),
    path('editartipo_recurso/<int:tipo_r_id>/', views.edit_tipo_recurso, name='edit_tipo_recurso'),
    path('eliminartipo_recurso/', views.delete_tipo_recurso, name='delete_tipo_recurso'),

    path('listarunidades/', views.list_unidades, name='list_unidades'),
    path('crearunidad/', views.create_unidad, name='create_unidad'),
    path('editarunidad/<int:unidad_id>/', views.edit_unidad, name='edit_unidad'),
    path('eliminarunidad/', views.delete_unidad, name='delete_unidad'),

    path('listarpersonal/', views.list_personal, name='list_personal'),
    path('crearpersonal/', views.create_personal, name='crear_personal'),
    path('editarpersonal/<int:personal_id>/', views.edit_personal, name='edit_personal'),
    path('eliminarpersonal/', views.delete_personal, name='delete_personal'),

    path('listarrecursos/', views.list_recursos, name='list_recursos'),
    path('crearrecurso/', views.create_recurso, name='create_recurso'),
    path('editarrecurso/<int:recurso_id>/', views.edit_recurso, name='edit_recurso'),
    path('eliminarrecurso/', views.delete_recurso, name='delete_recurso'),
]
