# Fruteria/urls.py

from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
  url(r'^$', views.index, name='index'),
  path('album/new', views.album_new, name='album_new'),
  path('album/<int:pk>/', views.album_detail, name='album_detail'),
  path('grupo/new', views.grupo_new, name='grupo_new'),
  path('grupo/<pk>/', views.grupo_detail, name='grupo_detail'),
  path('musico/new', views.musico_new, name='musico_new'),
  path('musico/<int:pk>/', views.album_detail, name='musico_detail'),
]