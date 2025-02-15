from django.shortcuts import get_object_or_404, render, redirect
from .forms import EtablissementForm
from .models import *

def create_etablissement(request):
   
    if request.method == 'POST':
        form = EtablissementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            
            return redirect('etablissements:etablissement_list')
    else:
        form = EtablissementForm()  
    
    return render(request, 'etablissements/create_etablissement.html', {'form': form})

def detail_etablissement(request, id):
    etablissement = get_object_or_404(Etablissement, id=id)
    return render(request, "etablissements/details_etablissement.html", {"etablissement": etablissement})

def etablissement_list(request):
    etablissements = Etablissement.objects.all()
    
    # Passer les établissements au template
    return render(request, 'etablissements/etablissements_list.html', {'etablissements': etablissements})

def modifier_etablissement(request, id):
    etablissement = get_object_or_404(Etablissement, id=id)
    if request.method == "POST":
        form = EtablissementForm(request.POST, request.FILES, instance=etablissement)
        if form.is_valid():
            form.save()
            return redirect("detail_etablissement", id=id)
    else:
        form = EtablissementForm(instance=etablissement)

    return render(request, "etablissements/modifier_etablissement.html", {"form": form, "etablissement": etablissement})

def supprimer_etablissement(request, id):
    etablissement = get_object_or_404(Etablissement, id=id)
    if request.method == "POST":
        etablissement.delete()
        return redirect("liste_etablissements")

    return render(request, "etablissements/supprimer_etablissement.html", {"etablissement": etablissement})