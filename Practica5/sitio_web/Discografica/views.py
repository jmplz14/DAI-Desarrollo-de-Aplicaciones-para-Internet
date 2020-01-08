# Discografica/views.py

from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import AlbumForm, MusicoForm, GrupoForm
from .models import Album, Grupo, Musico
from django.utils import timezone
from django.shortcuts import redirect


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
    return render(request, 'album_edit.html', {'form': form})

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
    return render(request, 'album_edit.html', {'form': form})

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
    return render(request, 'musico_edit.html', {'form': form})

def musico_edit(request, pk):
    musico = get_object_or_404(Musico, pk=pk)
    if request.method == "POST":
        form = MusicoForm(request.POST, instance=musico)
        if form.is_valid():
            form.save()
            return redirect('musico_list')
    else:
        form = MusicoForm(instance=musico)
    return render(request, 'musico_edit.html', {'form': form})

def musico_list(request):
    musico = Musico.objects.all()
    return render(request, 'musico_list.html', {'musico': musico})

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
    return render(request, 'grupo_edit.html', {'form': form})


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
    return render(request, 'grupo_edit.html', {'form': form})

def grupo_borrar(request, pk):
    Grupo.objects.get(pk=pk).delete()
        
    return redirect('grupo_list')