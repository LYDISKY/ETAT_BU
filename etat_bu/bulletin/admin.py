from django.contrib import admin
from .models import *

@admin.register(Bulletin)
class BulletinAdmin(admin.ModelAdmin):
    list_display = ('student', 'classe', 'etablissement', 'period', 'moyenne_generale', 'date_created')
    search_fields = ('student__nom', 'classe__sigle', 'etablissement__nom')
    list_filter = ('period', 'etablissement', 'classe')
    ordering = ('-date_created',)
    autocomplete_fields = ('student', 'classe', 'etablissement')
