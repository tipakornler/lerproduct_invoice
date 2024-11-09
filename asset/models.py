from django.db import models
import datetime

company_name = (
    ('LER_Co.','LER_Co'),
    ('TST_Co.', 'TST_Co'),
)

# Create your models here.
class asset(models.Model):
    asset_name = models.CharField(max_length=300, null=True, blank=True)
    company = models.CharField(max_length=20, choices=company_name, default='', null=True, blank=True)
    asset_price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    depreciation_year = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    purchase_reason = models.TextField(null=True, blank=True)
    purchase_date = models.DateField(default=datetime.date.today,blank=True, null=True)
    note = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)

