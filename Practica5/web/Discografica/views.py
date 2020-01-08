# Discografica/views.py

from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import AlbumForm, MusicoForm, GrupoForm
from .models import Album, Grupo, Musico
from django.utils import timezone
from django.shortcuts import redirect
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.core import serializers
import json


# Create your views here.


    
def index(request):
    return render(request,'index.html', {})

def album_list(request):
    album = Album.objects.all()
    return render(request, 'album_list.html', {'album': album})

def album_edit(request, pk):
    album = get_object_or_404(Album, pk=pk)
    if request.method == "POST":
        form = AlbumForm(request.POST, instance=album)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm(instance=album)
    nombre = form.Meta.model.__name__
    return render(request, 'edit.html', {'form': form, 'nombre': nombre})



def album_borrar(request, pk):
    album = get_object_or_404(Album, pk=pk)
    album.delete()
    #if request.method == "POST":
        
    return redirect('album_list')

def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('album_list')
    else:
        form = AlbumForm()
    nombre = form.Meta.model.__name__
    return render(request, 'edit.html', {'form': form, 'nombre': nombre})


def album_detail(request, pk):
    post = get_object_or_404(Album, pk=pk)
    return render(request, 'album_detail.html', {'post': post})

def musico_new(request):
    if request.method == "POST":
        form = MusicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('musico_list')
    else:
        form = MusicoForm()

    nombre = form.Meta.model.__name__
    return render(request, 'edit.html', {'form': form, 'nombre': nombre})




def musico_edit(request, pk):
    musico = get_object_or_404(Musico, pk=pk)
    if request.method == "POST":
        form = MusicoForm(request.POST, instance=musico)
        if form.is_valid():
            form.save()
            return redirect('musico_list')
    else:
        form = MusicoForm(instance=musico)

    nombre = form.Meta.model.__name__
    return render(request, 'edit.html', {'form': form, 'nombre': nombre})

def musico_list(request):
    datos = Musico.objects.all()
    
    cabecera = MusicoForm.Meta.fields
    return render(request, 'musico_list.html', {'datos': datos, 'cabecera': cabecera})

def musico_detail(request, pk):
    post = get_object_or_404(Musico, pk=pk)
    return render(request, 'musico_detail.html', {'post': post})

def musico_borrar(request, pk):
    musico = get_object_or_404(Musico, pk=pk)
    musico.delete()
         
    return redirect('musico_list')

def grupo_new(request):
    if request.method == "POST":
        form = GrupoForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('grupo_list')
    else:
        form = GrupoForm()

    nombre = form.Meta.model.__name__
    return render(request, 'edit.html', {'form': form, 'nombre': nombre})



def grupo_detail(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    return render(request, 'grupo_detail.html', {'grupo': grupo})

def grupo_list(request):
    grupo = Grupo.objects.all()
    return render(request, 'grupo_list.html', {'grupo': grupo})

def grupo_edit(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    if request.method == "POST":
        form = GrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            Grupo.objects.get(pk=pk).delete()
            form.save()
            return redirect('grupo_list')
    else:
        form = GrupoForm(instance=grupo)
    nombre = form.Meta.model.__name__
    return render(request, 'edit.html', {'form': form, 'nombre': nombre})

def grupo_borrar(request, pk):
    Grupo.objects.get(pk=pk).delete()
        
    return redirect('grupo_list')

def paginacion_no_ajax(request):
    datos = Musico.objects.all()
    
    cabecera = MusicoForm.Meta.fields
    return render(request, 'paginacion_sin_ajax.html', {'datos': datos, 'cabecera': cabecera})

def paginacion_con_ajax(request):
    pagina = 1
    datos = Musico.objects.all()
    inicio = (pagina - 1) * 5
    total = len(datos)
    i = 0
    datosMostrar = list()
    while (i < 5 and (inicio + i) < total ):
        datosMostrar.append(datos[inicio + i])
        i += 1
        
    paginas = list()
    paginas.append(1)
    numPaginas = total//5
    if numPaginas > 2:
        paginas.append(2)
    if numPaginas  > 3:
        paginas.append(3)
    

        
    cabecera = MusicoForm.Meta.fields
    
    return render(request, 'paginacion_con_ajax.html', {'datos': datosMostrar, 'cabecera': cabecera})

def obtener_pagina(request, pagina):
    datos = Musico.objects.all()
    inicio = (pagina - 1) * 5
    total = len(datos)
    i = 0
    datosMostrar = list()
    while (i < 5 and (inicio + i) < total ):
        datosMostrar.append(datos[inicio + i])
        i += 1
    serializado = serializers.serialize('json', datosMostrar)
    return JsonResponse({'datos': serializado, 'numElementos': total })

def obtener_total(request):
    datos = Musico.objects.all()
    total = len(datos)

    return JsonResponse({'numElementos': total })

def mapa(request):

    datos = Musico.objects.all()
    datos_musicos = list()
    for i in datos:
        valores = [i.nombre, i.coordenadaX, i.coordenadaY]
        datos_musicos.append(valores)


    return render(request, 'mapa.html', {'datos': datos})

def grafica(request):
    porcentajes = list()
    valores = list()
    total = 0

    musicos = Musico.objects.all()

    total += len(musicos) 

    grupos = Grupo.objects.all()
    
    total += len(grupos) 

    album = Album.objects.all()

    total += len(album)
    
    valores.append(len(musicos))
    valores.append(len(grupos))
    valores.append(len(album))
    porcentajes.append((len(musicos)/total)*100)
    porcentajes.append((len(grupos)/total)*100)
    porcentajes.append((len(album)/total)*100)

    return render(request, 'grafica.html',{'datos': porcentajes, 'valores': valores})