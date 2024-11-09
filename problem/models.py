from django.db import models
from invoice.models import invoice,invoice_product
from product.models import allproduct




class issue(models.Model):
    order_number = models.ForeignKey(invoice, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='issues')
    topic = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    user = models.CharField(max_length=300, null=True, blank=True)
    onprocess = models.BooleanField(default=False)
    status = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)