from django.db import models
from product.models import allproduct


# Create your models here.
class listpromo(models.Model):
    brandid = models.ForeignKey(allproduct, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='brandids')
    normal_price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    promotion_price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)

    




    