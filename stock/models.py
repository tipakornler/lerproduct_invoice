from django.db import models
from invoice.models import invoice
from product.models import allproduct
from django.db.models import Sum, FloatField, Value, F

class stockOnhand(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_number = models.ForeignKey(invoice, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='order_numbers')
    product = models.ForeignKey(allproduct, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='products')
    buy_price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    qty =  models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)

    @property
    def qtyout(self):
        return self.stockouts.all().aggregate(Sum('qty_out'))['qty_out__sum']




class stockout(models.Model):
    order_id = models.ForeignKey(stockOnhand, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='stockouts')
    order_number_out = models.ForeignKey(invoice, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='stockouts')
    sell_price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    qty_out =  models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)



# Create your models here.
