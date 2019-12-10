# Fruteria/views.py

from django.shortcuts import render, HttpResponse, get_object_or_404
from .forms import AlbumForm, MusicoForm, GrupoForm
from .models import Album, Grupo, Musico
from django.shortcuts import redirect

# Create your views here.

def index(request):
    return render(request,'index.html', {})


def album_new(request):
    if request.method == "POST":
        form = AlbumForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('album_detail', pk=post.pk)
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
            post = form.save()
            return redirect('musico_detail', pk=post.pk)
    else:
        form = MusicoForm()
    return render(request, 'musico_edit.html', {'form': form})

def grupo_new(request):
    if request.method == "POST":
        form = GrupoForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('grupo_detail', pk=post.pk)
    else:
        form = GrupoForm()
    return render(request, 'grupo_edit.html', {'form': form})

def grupo_detail(request, pk):
    grupo = get_object_or_404(Grupo, pk=pk)
    return render(request, 'grupo_detail.html', {'grupo': grupo})