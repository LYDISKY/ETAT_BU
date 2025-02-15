from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('ajouter/professeur/', ajouter_personne, {'role': 'PROFESSEUR'}, name='ajouter_professeur'),
    path('ajouter/etudiant/', ajouter_personne, {'role': 'ETUDIANT'}, name='ajouter_etudiant'),
    path('ajouter/secretaire/', ajouter_personne, {'role': 'SECRETAIRE'}, name='ajouter_secretaire'),
    path('', liste_personnes, name='liste_personnes'),
    path('details/<int:pk>/', details_personne, name='details_personne'),
    path('modifier/<int:pk>/', PersonneUpdateView.as_view(), name='modifier_personne'),
    path('supprimer/<int:pk>/', PersonneDeleteView.as_view(), name='supprimer_personne'),
]