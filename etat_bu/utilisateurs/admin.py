from django.contrib import admin
from .models import *

class PersonneAdmin(admin.ModelAdmin):
    fields = ['last_name', 'id_eta', 'first_name', 'email', 'password', 'tel', 'role','created_at']
    list_display = ['last_name', 'first_name', 'email', 'tel', 'role', 'created_at']  # Optionnel pour l'affichage en liste
    search_fields = ['last_name', 'first_name', 'email']  # Optionnel pour ajouter une recherche
    readonly_fields = ['created_at']

admin.site.register(Personne, PersonneAdmin)