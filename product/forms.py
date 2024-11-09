from django import forms
from .models import ContactForm

class contactform(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ('contact_name','contact_email', 'contact_message')