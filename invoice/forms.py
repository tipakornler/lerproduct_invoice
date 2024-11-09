from django import forms
from .models import invoice_product

class CheckPaymentForm(forms.ModelForm):
    class Meta:
        model = invoice_product
        fields = ('paymentmade','money_collect')