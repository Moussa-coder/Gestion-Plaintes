from django.urls import path
from . import views

urlpatterns = [
    path('accueil/', views.accueil_citoyen, name='accueil_citoyen'),
    path('deposer/', views.deposer_plainte, name='deposer_plainte'),
    path('modifier_plainte_et_statut/<int:plainte_id>/', views.modifier_plainte_et_statut, name='modifier_plainte_et_statut'),
    path('mes_plaintes/', views.mes_plaintes, name='mes_plaintes'),
]

