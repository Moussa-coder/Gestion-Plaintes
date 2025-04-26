from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('L\'adresse email est obligatoire')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom


class Statut(models.Model):
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Plainte(models.Model):
    citoyen = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='plaintes')
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    description = models.TextField()
    localisation = models.CharField(max_length=255)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    photo = models.ImageField(upload_to='plaintes/', null=True, blank=True)
    date_heure = models.DateTimeField(auto_now_add=True)
    statut = models.ForeignKey(Statut, on_delete=models.CASCADE)

    def __str__(self):
        return f"Plainte de {self.citoyen.email} - {self.categorie.nom}"
