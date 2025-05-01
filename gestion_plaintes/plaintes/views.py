from django.shortcuts import get_object_or_404, render, redirect
from .forms import CommentaireForm, PlainteForm
from django.contrib.auth.decorators import login_required
from .models import Plainte, Statut
from .untils import envoyer_notification_utilisateur  # Import de la fonction

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

@login_required
def mes_plaintes(request):
    plaintes = Plainte.objects.filter(utilisateur=request.user).order_by('-date_creation')
    return render(request, 'plaintes/mes_plaintes.html', {'plaintes': plaintes})

@login_required
def modifier_plainte_et_statut(request, plainte_id):
    plainte = get_object_or_404(Plainte, id=plainte_id, utilisateur=request.user)
    statuts = Statut.objects.all()

    if request.method == 'POST':
        form = PlainteForm(request.POST, request.FILES, instance=plainte)
        statut_id = request.POST.get('statut')
        if form.is_valid() and statut_id:
            statut_nouveau = get_object_or_404(Statut, id=statut_id)

            plainte = form.save(commit=False)
            if plainte.statut != statut_nouveau:
                plainte.statut = statut_nouveau
                envoyer_notification_utilisateur(plainte)
            plainte.save()

            return redirect('mes_plaintes')
    else:
        form = PlainteForm(instance=plainte)

    return render(request, 'plaintes/modifier_plainte.html', {
        'form': form,
        'plainte': plainte,
        'statuts': statuts
    })

@login_required
def ajouter_commentaire(request, plainte_id):
    plainte = get_object_or_404(Plainte, id=plainte_id)
    if request.method == 'POST':
        form = CommentaireForm(request.POST)
        if form.is_valid():
            commentaire = form.save(commit=False)
            commentaire.plainte = plainte
            commentaire.admin = request.user
            commentaire.save()
            return redirect('mes_plaintes')
    else:
        form = CommentaireForm()
    
    return render(request, 'plaintes/ajouter_commentaire.html', {'form': form, 'plainte': plainte})