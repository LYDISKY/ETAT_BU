from django import forms
from .models import *


class PersonneForm(forms.ModelForm):
    class Meta:
        model = Personne
        fields = ['last_name', 'first_name', 'email', 'tel', 'id_eta', 'password']

    def __init__(self, *args, **kwargs):
        initial_role = kwargs.pop('initial_role', None)  # Récupère le rôle passé
        super().__init__(*args, **kwargs)
        if initial_role:
            self.instance.role = initial_role

