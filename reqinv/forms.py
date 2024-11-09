from django import forms
from .models import reqinv

class reqinvForm(forms.ModelForm):
    class Meta:
        model = reqinv
        fields = ('order_m','name','tel_number','address','postcode','tax_id','platform','invoice_product','email','price','user')