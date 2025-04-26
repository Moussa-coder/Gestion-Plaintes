from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class CitoyenInscriptionForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone', 'password1', 'password2')

class CitoyenConnexionForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(CitoyenConnexionForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Email"
        self.fields['username'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Mot de passe'