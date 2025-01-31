from django.contrib import admin
from .models import *

@admin.register(Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    list_display = ('nom', 'type_etablissement', 'decoupage_annuel', 'adresse', 'contact')
    list_filter = ('type_etablissement', 'decoupage_annuel')
    search_fields = ('nom', 'adresse')
 