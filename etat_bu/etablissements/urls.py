from django.urls import path
from . import views

app_name = 'etablissements'

urlpatterns = [
   
    path('create/', views.create_etablissement, name='create_etablissement'),
    path('list/', views.etablissement_list, name='etablissement_list'),
]