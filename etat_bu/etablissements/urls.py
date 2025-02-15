from django.urls import path
from .views import *

urlpatterns = [
    path('create/',create_etablissement, name='create_etablissement'),
    path('list/',etablissement_list, name='etablissement_list'),
    path('<int:id>/', detail_etablissement, name='detail_etablissement'),
    path('modifier/<int:id>/', modifier_etablissement, name='modifier_etablissement'),
    path('supprimer/<int:id>/', supprimer_etablissement, name='supprimer_etablissement'),
]