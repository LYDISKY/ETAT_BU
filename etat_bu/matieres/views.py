from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


#*********** CLASSES ************


# Liste des classes
def liste_classes(request):
    classes = Classe.objects.all()
    return render(request, 'classe/liste_classes.html', {'classes': classes})

# Détails d'une classe
def details_classe(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    return render(request, 'classe/details_classe.html', {'classe': classe})

# Ajouter une classe
def ajouter_classe(request):
    if request.method == 'POST':
        form = ClasseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_classes')
    else:
        form = ClasseForm()
    return render(request, 'classe/ajouter_classe.html', {'form': form})

# Modifier une classe
def modifier_classe(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        form = ClasseForm(request.POST, instance=classe)
        if form.is_valid():
            form.save()
            return redirect('liste_classes')
    else:
        form = ClasseForm(instance=classe)
    return render(request, 'classe/modifier_classe.html', {'form': form})

# Supprimer une classe
def supprimer_classe(request, pk):
    classe = get_object_or_404(Classe, pk=pk)
    if request.method == 'POST':
        classe.delete()
        return redirect('liste_classes')
    return render(request, 'classe/supprimer_classe.html', {'classe': classe})


# ********** MATIERES ***********


def liste_matieres(request):
    matieres = Matiere.objects.all()
    return render(request, 'matieres/matiere_list.html', {'matieres': matieres})

def detail_matiere(request, pk):
    matiere = get_object_or_404(Matiere, pk=pk)
    return render(request, 'matieres/matiere_detail.html', {'matiere': matiere})

def creer_matiere(request):
    if request.method == "POST":
        form = MatiereForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('matiere_list')
    else:
        form = MatiereForm()
    return render(request, 'matieres/matiere_create.html', {'form': form})

def modifier_matiere(request, pk):
    matiere = get_object_or_404(Matiere, pk=pk)
    if request.method == "POST":
        form = MatiereForm(request.POST, instance=matiere)
        if form.is_valid():
            form.save()
            return redirect('matiere_list')
    else:
        form = MatiereForm(instance=matiere)
    return render(request, 'matieres/matiere_form.html', {'form': form})

def supprimer_matiere(request, pk):
    matiere = get_object_or_404(Matiere, pk=pk)
    if request.method == "POST":
        matiere.delete()
        return redirect('matiere_list')
    return render(request, 'matieres/matiere_confirm_delete.html', {'matiere': matiere})
