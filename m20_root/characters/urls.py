from django.urls import path
from . import views

urlpatterns = [
    path('',
         views.CharacterListView.as_view(), name='index'),
    path(
        'characters/<slug:slug>/',
        views.CharacterDetailView.as_view(), name='character_detail'),
]
