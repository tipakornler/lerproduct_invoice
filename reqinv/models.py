from django.db import models
from invoice.models import invoice
from product.models import allproduct




class reqinv(models.Model):
    order_m = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    tel_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    postcode = models.CharField(max_length=5, null=True, blank=True)
    tax_id = models.CharField(max_length=13, null=True, blank=True)
    platform = models.CharField(max_length=13, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    invoice_product = models.CharField(max_length=300, null=True, blank=True)
    user = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)