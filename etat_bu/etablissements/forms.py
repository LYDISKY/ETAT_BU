from django import forms
from .models import Etablissement

class EtablissementForm(forms.ModelForm):
    class Meta:
        model = Etablissement
        fields = ['name', 'code', 'address', 'contact', 'logo', 'type_etablissement', 'decoupage_annuel']
