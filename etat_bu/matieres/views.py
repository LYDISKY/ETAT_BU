from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

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
