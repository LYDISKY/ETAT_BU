from django.contrib import admin
from .models import *

class PersonneAdmin(admin.ModelAdmin):
    fields = ['last_name', 'id_eta', 'first_name', 'email', 'password', 'tel', 'role','created_at']
    list_display = ['last_name', 'first_name', 'email', 'tel', 'role', 'created_at']  
    search_fields = ['last_name', 'first_name', 'email']
    readonly_fields = ['created_at']

admin.site.register(Personne, PersonneAdmin)

