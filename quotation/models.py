from re import S
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from product.models import allproduct, Brand
from django.db.models import Sum, FloatField, Value, F
from decimal import Decimal
import datetime


class quotation(models.Model):
    name = models.CharField(max_length=300, null=True, blank=True)
    tel_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    tax_number = models.CharField(max_length=50, null=True, blank=True)
    email_addess = models.CharField(max_length=50, null=True, blank=True)
    quotation_date = models.DateField(default=datetime.date.today,blank=True, null=True)
    buy_item = models.BooleanField(default=False, help_text="ลูกค้าซื้อหรือเปล่า")
    brance = models.CharField(max_length=300, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)

    def __str__(self):
        return '%s' % self.name

    class Meta:
        ordering = ('name', )
        index_together = (('id', 'tel_number'),)


    def get_quo(self):
        return reverse('quo_vat', args=[self.id, 7878])


    @property
    def number_str(self):
        return f'{self.id}_{self.tel_number}'



class quotation_product(models.Model):
    name = models.ForeignKey(quotation, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='quos')
    product = models.ForeignKey(allproduct, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='quos')
    brand   = models.ForeignKey(Brand,null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='quos')
    qty =  models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    sell_price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, help_text="จำนวนเงินที่ออกบิล")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)