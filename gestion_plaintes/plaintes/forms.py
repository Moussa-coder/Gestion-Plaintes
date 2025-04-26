from django import forms
from .models import Plainte

class PlainteForm(forms.ModelForm):
    class Meta:
        model = Plainte
        fields = ['categorie', 'description', 'photo', 'localisation']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
