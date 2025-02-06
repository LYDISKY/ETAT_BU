from django.urls import path
from .views import *
urlpatterns = [
   path('Classe/', liste_classes, name='liste_classes'),
    path('Classe/details/<int:pk>/', details_classe, name='details_classe'),
    path('Classe/ajouter/', ajouter_classe, name='ajouter_classe'),
    path('Classe/modifier/<int:pk>/',modifier_classe, name='modifier_classe'),
    path('Classe/supprimer/<int:pk>/',supprimer_classe, name='supprimer_classe'),


]