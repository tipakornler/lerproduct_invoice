from multiprocessing.dummy import active_children
from django.db import models
# from fastapi import BackgroundTasks
from product.models import Brand

# Added on Oct 14,2022 -- To increase Used on promotion when Order created.
from django.db.models.signals import post_save,pre_save

# Create your models here.
class code(models.Model):
    name            = models.CharField(max_length=10,primary_key=True)#ABC090
    decription      = models.TextField()
    total           = models.IntegerField(default=1)
    used            = models.IntegerField(default=0)
    start 			= models.DateField(null=True, blank=True)
    stop 			= models.DateField(null=True, blank=True)
    discount_rate 	= models.DecimalField(default=0,max_digits=10, decimal_places=2,null=True, blank=True)#%
    discount_price 	= models.DecimalField(default=0,max_digits=10, decimal_places=2,null=True, blank=True)#Price
    # Level
    activated       = models.BooleanField(default=False)
    show            = models.BooleanField(default=False)
    # Added on Oct 3,2022 -- To support more promotion criteria.
    promo_price     = models.IntegerField(default=10_000) #price for enable promotion, default 10,000 Baht
    brands          = models.ManyToManyField(Brand)

    def __str__(self):
        return f'{self.name} {self.discount_rate} %' 

# Added on Oct 14,2022 -- To increase Used on promotion when Order created.
# Edit on Oct 18,2022 -- To fix activated is not reset if Used=Total.
def code_save(sender, instance, **kwargs):
    if (instance.used >= instance.total) and instance.activated :
        instance.activated = False
        instance.save()

pre_save.connect(code_save, sender=code)
# --------------------------------------------------------------------
