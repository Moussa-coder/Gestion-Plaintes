from django.contrib import admin
from .models import Categorie, Statut, Plainte

# Enregistrement des modèles dans l'admin
admin.site.register(Categorie)
admin.site.register(Statut)
admin.site.register(Plainte)
