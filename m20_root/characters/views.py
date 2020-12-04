from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Character

# Create your views here.


def index(request):
    return HttpResponse("<h1>microlite20 Characters</h1>")


class CharacterDetailView(generic.DetailView):
    model = Character
    template_name = 'characters/character_detail.html'


class CharacterListView(generic.ListView):
    model = Character
    template_name = 'characters/index.html'
