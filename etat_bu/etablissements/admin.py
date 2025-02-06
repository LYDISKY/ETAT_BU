from django.contrib import admin
from .models import *

@admin.register(Etablissement)
class EtablissementAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'type_etablissement', 'decoupage_annuel', 'address', 'contact', 'created_at')
    list_filter = ('type_etablissement', 'decoupage_annuel')
    search_fields = ('name', 'address','code')
 