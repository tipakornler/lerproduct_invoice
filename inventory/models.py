from django.db import models
from invoice.models import invoice
from product.models import allproduct,Brand
from django.db.models import Sum, FloatField, Value, F


class locationInventory(models.Model):
       location = models.CharField(max_length=300, null=True, blank=True, unique=True)
       address = models.TextField(null=True, blank=True)

       def __str__(self):
        return '%s' % self.location

class ProductInventory(models.Model):
        product = models.ForeignKey(allproduct, null=True,blank = True,
                on_delete=models.SET_NULL,
                related_name='productinventorys')
        brand = models.ForeignKey(Brand, null=True,blank = True,
                on_delete=models.SET_NULL,
                related_name='productinventorys')
        status = models.BooleanField(default=True)   
        created = models.DateTimeField(auto_now_add=True)
        updated = models.DateTimeField(blank=True, null=True,auto_now=True)

        def __str__(self):
                return '%s' % self.product

        @property
        def qty_in(self):
                return self.inventoryins.all().aggregate(Sum('qty'))['qty__sum'] 
        
        @property
        def qty_out(self):
                return self.inventoryouts.all().aggregate(Sum('qty'))['qty__sum'] 
        
        def qty_sum(self):
               return self.qty_in-self.qty_out if self.qty_out and self.qty_in != None else 0


class InventoryIn(models.Model):
    productin = models.ForeignKey(ProductInventory, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='inventoryins') 
    order_number = models.ForeignKey(invoice, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='inventoryins')
    location = models.ForeignKey(locationInventory, null=True,blank = True,
            on_delete=models.SET_NULL,default=1,
            related_name='inventoryins')
    buy_price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    qty =  models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)



class InventoryOut(models.Model):
    productout = models.ForeignKey(ProductInventory, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='inventoryouts')
    order_number = models.ForeignKey(invoice, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='inventoryouts')
    qty =  models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)