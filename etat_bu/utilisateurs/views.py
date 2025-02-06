from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .forms import *
from .models import Personne

def ajouter_personne(request, role):

    """Vue  pour ajouter une personne avec un rôle prédéfini."""

    if request.method == "POST":
        form = PersonneForm(request.POST, initial_role=role)  
        if form.is_valid():
            personne = form.save(commit=False)
            personne.role = role  
            personne.save()
            messages.success(request, f"{role} ajouté avec succès !")
            return redirect("liste_personnes")
    else:
        form = PersonneForm(initial_role=role)  

    return render(request, "utilisateurs/ajouter_personne.html", {"form": form, "role": role})

def liste_personnes(request):

    """Affiche la liste de toutes les personnes enregistrées."""

    personnes = Personne.objects.all()
    return render(request, "utilisateurs/liste_personnes.html", {"personnes": personnes})

def details_personne(request, pk):
    # Récupérer l'utilisateur à afficher avec son ID
    personne = get_object_or_404(Personne, pk=pk)
    return render(request, 'utilisateurs/details_personne.html', {'personne': personne})

 
class PersonneUpdateView(UpdateView):
    model = Personne
    form_class = PersonneForm
    template_name = 'utilisateurs/modifier_personne.html'
    success_url = reverse_lazy('liste_personnes')  

    def get_object(self, queryset=None):
        """Récupère l’utilisateur à modifier avec son ID"""
        return get_object_or_404(Personne, pk=self.kwargs['pk'])

@method_decorator(login_required, name='dispatch')
class PersonneDeleteView(DeleteView):
    model = Personne
    template_name = 'utilisateurs/confirmer_suppression.html'
    success_url = reverse_lazy('liste_personnes')  # Redirection après suppression

    def get_object(self, queryset=None):
        """Empêche un utilisateur de supprimer son propre compte"""
        obj = super().get_object(queryset)
        if self.request.user == obj:
            raise PermissionDenied("Vous ne pouvez pas supprimer votre propre compte.")
        return obj





