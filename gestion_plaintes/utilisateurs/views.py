from django.shortcuts import render, redirect
from .forms import CitoyenInscriptionForm, CitoyenConnexionForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

def inscription(request):
    if request.method == 'POST':
        form = CitoyenInscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('connexion')  
    else:
        form = CitoyenInscriptionForm()
    return render(request, 'utilisateurs/inscription.html', {'form': form})

def connexion(request):
    if request.method == 'POST':
        form = CitoyenConnexionForm(request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('accueil')  # tu peux créer une page d'accueil après
    else:
        form = CitoyenConnexionForm()
    return render(request, 'utilisateurs/connexion.html', {'form': form})

@login_required
def deconnexion(request):
    logout(request)
    return redirect('connexion')
