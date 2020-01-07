# Discografica/urls.py

from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
  url(r'^$', views.index, name='index'),
  path('album/new', views.album_new, name='album_new'),
  path('album/<int:pk>/', views.album_detail, name='album_detail'),
  path('album/list',views.album_list, name='album_list'),
  path('album/<int:pk>/edit/', views.album_edit, name='album_edit'),
  path('album/<int:pk>/borrar/', views.album_borrar, name='album_borrar'),

  path('grupo/new', views.grupo_new, name='grupo_new'),
  path('grupo/<pk>/', views.grupo_detail, name='grupo_detail'),
  path('grupo/list', views.grupo_list, name='grupo_list'),
  path('grupo/<pk>/edit/', views.grupo_edit, name='grupo_edit'),
  path('grupo/<pk>/borrar/', views.grupo_borrar, name='grupo_borrar'),
  
  path('musico/new', views.musico_new, name='musico_new'),
  path('musico/<int:pk>/', views.musico_detail, name='musico_detail'),
  path('musico/list',views.musico_list, name='musico_list'),
  path('musico/<int:pk>/edit/', views.musico_edit, name='musico_edit'),
  path('musico/<int:pk>/borrar/', views.musico_borrar, name='musico_borrar'),
  
]