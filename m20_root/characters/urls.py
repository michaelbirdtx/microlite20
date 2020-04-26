from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'characters/<slug:slug>/',
        views.CharacterDetailView.as_view(), name='character_detail'),
]
