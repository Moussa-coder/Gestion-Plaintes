from django.shortcuts import render, redirect
from .forms import PlainteForm
from django.contrib.auth.decorators import login_required

@login_required
def accueil_citoyen(request):
    return render(request, 'plaintes/accueil.html', {'user': request.user})

@login_required
def deposer_plainte(request):
    if request.method == 'POST':
        form = PlainteForm(request.POST, request.FILES)
        if form.is_valid():
            plainte = form.save(commit=False)
            plainte.utilisateur = request.user
            plainte.save()
            return redirect('mes_plaintes')
    else:
        form = PlainteForm()
    return render(request, 'plaintes/deposer_plainte.html', {'form': form})
