from django.db import models
from django.conf import settings

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Statut(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Plainte(models.Model):
    utilisateur = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categorie, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    photo = models.ImageField(upload_to='plaintes/', blank=True, null=True)
    localisation = models.CharField(max_length=255, blank=True)
    statut = models.ForeignKey(Statut, on_delete=models.SET_NULL, null=True)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Plainte {self.id} par {self.utilisateur.username}"

class Commentaire(models.Model):
    plainte = models.ForeignKey(Plainte, on_delete=models.CASCADE)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    commentaire = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.admin.username} sur plainte {self.plainte.id}"
