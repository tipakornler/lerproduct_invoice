from django.db import models



# Create your models here.
class new(models.Model):
    product_id = models.CharField(max_length=300, null=True, blank=True)
    product_name = models.CharField(max_length=300, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    link_product = models.CharField(max_length=300, null=True, blank=True)
    youtube_link = models.CharField(max_length=500, null=True, blank=True)
    status_create = models.BooleanField(default=False)
    status_shopee = models.BooleanField(default=False)
    status_lazada = models.BooleanField(default=False)
    status_nocnoc = models.BooleanField(default=False)
    status_tiktok = models.BooleanField(default=False)
    status_mainweb = models.BooleanField(default=False)
    vdo = models.BooleanField(default=False)
    low_quality = models.BooleanField(default=False)
    comment = models.CharField(max_length=300, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)