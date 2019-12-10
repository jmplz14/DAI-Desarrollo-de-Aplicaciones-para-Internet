from django import forms
from .models import Album, Grupo, Musico
from django.shortcuts import redirect

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('titulo', 'distribuidora', 'fechaLanzamiento', 'grupo')

class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo
        fields = ('nombre', 'fechaCreacion', 'estilo')
        
class MusicoForm(forms.ModelForm):
    class Meta:
        model = Musico
        fields = ('nombre', 'fechaNacimiento', 'instrumentoPrincipal', 'grupo') 