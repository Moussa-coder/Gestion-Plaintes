from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def accueil_citoyen(request):
    return render(request, 'plaintes/accueil.html', {'user': request.user})
