from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .forms import EtablissementForm
from .models import *




def is_admin(user):
    return user.is_superuser

@user_passes_test(is_admin)
def create_etablissement(request):
   
    if request.method == 'POST':
        form = EtablissementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  
            
            return redirect('etablissements:etablissement_list')
    else:
        form = EtablissementForm()  
    
    return render(request, 'etablissements/create_etablissement.html', {'form': form})


def etablissement_list(request):
    etablissements = Etablissement.objects.all()
    
    # Passer les établissements au template
    return render(request, 'etablissements/etablissement_list.html', {'etablissements': etablissements})

