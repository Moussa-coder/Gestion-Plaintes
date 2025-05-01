from django.core.mail import send_mail
from django.conf import settings

def envoyer_notification_utilisateur(plainte):
    subject = f"Statut de votre plainte {plainte.id} a changé"
    message = f"Le statut de votre plainte {plainte.id} est désormais '{plainte.statut.nom}'."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [plainte.utilisateur.email]
    
    send_mail(subject, message, from_email, recipient_list)
