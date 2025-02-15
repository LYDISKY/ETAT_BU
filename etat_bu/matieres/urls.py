from django.urls import path
from .views import *
urlpatterns = [
    path('Classe/', liste_classes, name='liste_classes'),
    path('Classe/details/<int:pk>/', details_classe, name='details_classe'),
    path('Classe/ajouter/', ajouter_classe, name='ajouter_classe'),
    path('Classe/modifier/<int:pk>/',modifier_classe, name='modifier_classe'),
    path('Classe/supprimer/<int:pk>/',supprimer_classe, name='supprimer_classe'),

    path('matieres/', liste_matieres, name='matiere_list'),
    path('matieres/creer/', creer_matiere, name='creer_matiere'),
    path('matieres/<int:pk>/', detail_matiere, name='detail_matiere'),
    path('matieres/<int:pk>/modifier/', modifier_matiere, name='modifier_matiere'),
    path('matieres/<int:pk>/supprimer/', supprimer_matiere, name='supprimer_matiere'),
]