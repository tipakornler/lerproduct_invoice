from django import forms
from .models import Order, Payment


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'tel', 'email', 'address', 'postal_code', 'note','grand_price','promocode']

class payment(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ('payer_name', 'payer_among', 'payer_time','payer_date')

# class pay_later(forms.ModelForm):
#     class Meta:
#         model = Payment
#         fields = ('payer_name', 'total_need_to_paid')