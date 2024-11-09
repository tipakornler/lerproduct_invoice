from django import forms
from .models import new

class newpForm(forms.ModelForm):
    class Meta:
        model = new
        fields = ('product_id','product_name','price','link_product','comment')