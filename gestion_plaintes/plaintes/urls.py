from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.accueil_citoyen, name='accueil_citoyen'),
    path('deposer/', views.deposer_plainte, name='deposer_plainte'),
]

