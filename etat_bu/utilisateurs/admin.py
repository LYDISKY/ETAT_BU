from django.contrib import admin
from .models import *

class PersonneAdmin(admin.ModelAdmin):
    fields = ['nom', 'id_eta', 'prenom', 'email', 'password', 'telephone', 'role','created_at']
    list_display = ['nom', 'prenom', 'email', 'telephone', 'role', 'created_at']  # Optionnel pour l'affichage en liste
    search_fields = ['nom', 'prenom', 'email']  # Optionnel pour ajouter une recherche
    readonly_fields = ['created_at']

admin.site.register(Personne, PersonneAdmin)