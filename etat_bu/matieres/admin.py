from django.contrib import admin
from .models import *

@admin.register(Classe)
class ClasseAdmin(admin.ModelAdmin):
    list_display = ('code', 'name', 'strength', 'institution', 'class_teacher')  
    search_fields = ('code', 'name', 'institution__nom')
    list_filter = ('institution',)  
    ordering = ('code','name')  
    autocomplete_fields = ('institution', 'class_teacher')



@admin.register(Matiere)
class MatiereAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'coefficient', 'institution', 'teacher')  
    search_fields = ('name', 'code', 'institution__nom')  
    list_filter = ('institution',)  
    ordering = ('name',)
    autocomplete_fields = ('institution', 'teacher')


@admin.register(Notation)
class NotationAdmin(admin.ModelAdmin):
    list_display = ('student', 'matiere', 'class_assigned', 'score', 'max_score', 'evaluation_type', 'date_added')
    search_fields = ('student__nom', 'matiere__name', 'class_assigned__sigle')
    list_filter = ('evaluation_type', 'matiere', 'class_assigned')
    ordering = ('-date_added',)
    autocomplete_fields = ('student', 'matiere', 'class_assigned')

