from django.db import models
from product.models import allproduct
from promocode.models import code


class Order(models.Model):
    first_name = models.CharField(max_length=60)
    tel = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)
    address = models.CharField(max_length=150)
    postal_code = models.CharField(max_length=30)
    note = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    updated = models.DateTimeField(auto_now=True,null=True, blank=True)
    paid = models.BooleanField(default=False,null=True, blank=True)
    # Added by Chutchai on Oct 7,2022 -- To keep grand total price after promotion
    # and keep promotion code
    grand_price =  models.DecimalField(default=0,max_digits=10, 
                    decimal_places=2,null=True, blank=True)
    promocode   = models.ForeignKey(code,null=True, blank=True,
                    on_delete=models.SET_NULL,related_name='orders')

    class Meta:
        ordering = ('-created', )

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(allproduct, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

class Payment(models.Model):
    payer_name = models.CharField(max_length=100)
    payer_among = models.DecimalField(max_digits=19, decimal_places=0,null=True, blank=True)
    total_need_to_paid = models.CharField(max_length=100, null=True, blank=True)
    paid = models.BooleanField(default=False,null=True, blank=True)
    payer_time = models.CharField(max_length=100,null=True, blank=True)
    payer_date = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return self.payer_name