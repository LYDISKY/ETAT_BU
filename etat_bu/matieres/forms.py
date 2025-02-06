from django import forms
from .models import *


class ClasseForm(forms.ModelForm):
    class Meta:
        model = Classe
        fields = ['name', 'code', 'strength', 'institution', 'class_teacher']

         # Filtrer pour ne montrer que les professeurs
    class_teacher = forms.ModelChoiceField(
        queryset=Personne.objects.filter(role='PROFESSEUR').exclude(role='ETUDIANT'),
        required=False,  
        label='Enseignant',
        empty_label="Sélectionner un Professeur"  
    )