from re import S
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from product.models import allproduct, Brand
from django.db.models import Sum, FloatField, Value, F
from decimal import Decimal
import datetime
from django_resized import ResizedImageField



def receive_img(instance, filename):
	return 'files/recive/%s/%s' % (instance.tel_number, filename)

def map_img(instance, filename):
	return 'files/map/%s/%s' % (instance.tel_number, filename)

def signature_img(instance, filename):
	return 'files/signature/%s/%s' % (instance.tel_number, filename)

def pic1_img(instance, filename):
	return 'files/pic1/%s/%s' % (instance.tel_number, filename)

def pic2_img(instance, filename):
	return 'files/pic2/%s/%s' % (instance.tel_number, filename)

def pic3_img(instance, filename):
	return 'files/pic3/%s/%s' % (instance.tel_number, filename)

def pic4_img(instance, filename):
	return 'files/pic4/%s/%s' % (instance.tel_number, filename)

def pic5_img(instance, filename):
	return 'files/pic5/%s/%s' % (instance.tel_number, filename)

def pic6_img(instance, filename):
	return 'files/pic6/%s/%s' % (instance.tel_number, filename)

class invoice(models.Model):
    order_number = models.CharField(max_length=300, null=True, blank=True, unique=True)
    overall = models.TextField(null=True, blank=True)
    overall_invoice = models.TextField(null=True, blank=True)
    name = models.CharField(max_length=300, null=True, blank=True)
    name_invoce = models.CharField(max_length=300, null=True, blank=True)
    tel_number = models.CharField(max_length=50, null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    address_invoice = models.TextField(null=True, blank=True)
    tax_number = models.CharField(max_length=50, null=True, blank=True)
    email_addess = models.CharField(max_length=50, null=True, blank=True)
    invoice_date = models.DateField(default=datetime.date.today,blank=True, null=True)
    billable = models.BooleanField(default=False)
    ler_pickup = models.BooleanField(default=False, help_text="ไปรับสินค้าเอง")
    ler_receive = models.CharField(max_length=100,null=True, blank=True)
    ler_deliver = models.CharField(max_length=100,null=True, blank=True)
    ler_print = models.BooleanField(default=False)
    ler_note = models.TextField(null=True, blank=True,help_text="ข้อความถึงขนส่ง")
    ler_expected_d = models.CharField(max_length=100,null=True, blank=True)
    ler_priority = models.IntegerField(null=True, blank=True)
    ler_map = models.CharField(max_length=100,null=True, blank=True)

    ler_pic1 = ResizedImageField(scale=0.7, quality=60,upload_to=pic1_img, max_length=500, null=True, blank=True )
    def __str__(self):
        return self.name
    ler_pic2 = ResizedImageField(scale=0.7, quality=60,upload_to=pic2_img, max_length=500, null=True, blank=True )
    def __str__(self):
        return self.name
    ler_pic3 = ResizedImageField(scale=0.7, quality=60,upload_to=pic3_img, max_length=500, null=True, blank=True )
    def __str__(self):
        return self.name
    ler_pic4 = ResizedImageField(scale=0.7, quality=60,upload_to=pic4_img, max_length=500, null=True, blank=True )
    def __str__(self):
        return self.name
    ler_pic5 = ResizedImageField(scale=0.7, quality=60,upload_to=pic5_img, max_length=500, null=True, blank=True )
    def __str__(self):
        return self.name
    ler_pic6 = ResizedImageField(scale=0.7, quality=60,upload_to=pic6_img, max_length=500, null=True, blank=True )
    def __str__(self):
        return self.name
    invoice_etax = models.BooleanField(default=False, help_text="ลูกค้าต้องการออก e-tax")
    invoice = models.BooleanField(default=True , help_text="ถ้าเก็บ stock ไม่ต้องใส่")
    paid = models.BooleanField(default=False)
    invoice_eve = models.CharField(max_length=50, null=True, blank=True)
    count_invoice_number = models.CharField(max_length=9, null=True, blank=True)
    invoice_tst = models.CharField(max_length=9, null=True, blank=True)
    print_tst = models.BooleanField(default=False)
    delivery_date = models.CharField(max_length=100,null=True, blank=True)
    evenote = models.TextField(null=True, blank=True, help_text="ข้อความถึง supplier")
    comment = models.CharField(max_length=50,null=True, blank=True, help_text="เลข edi")
    comment2 = models.CharField(max_length=50,null=True, blank=True, help_text="ติดตั้ง/ไม่ติดตั้ง")
    comment3 = models.TextField(null=True, blank=True, help_text="ข้อความถึง supplier3")
    map_pic = models.ImageField(upload_to=map_img, max_length=500, null=True, blank=True,help_text="แผนที่" )
    def __str__(self):
        return self.name
    receive_pic = models.ImageField(upload_to=receive_img, max_length=500, null=True, blank=True ,help_text="ใบเสร็จ" )
    def __str__(self):
        return self.name
    brance = models.CharField(max_length=300, null=True, blank=True, help_text="สาขากรณ๊ไม่ใช่สำนักงานใหญ่")
    etax = models.BooleanField(default=False, help_text="ส่ง/ออก e-tax แล้ว")
    urgent_need_invoice = models.BooleanField(default=False)
    send_etax_email = models.BooleanField(default=True)
    cancel_inv = models.BooleanField(default=False)
    cancel_date = models.DateField(blank=True, null=True , help_text="วันที่ยกเลิก")
    showroom = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)

    def __str__(self):
        return '%s' % self.order_number


    def get_po(self):
        return reverse('po', args=[self.id, 7878])

    def get_absolute_url(self):
        return reverse('primary', args=[self.id, self.tel_number])

    def get_secondary(self):
        return reverse('secondary', args=[self.id, 6464])

    def get_primary_tst(self):
        return reverse('primarytst', args=[self.id, self.tel_number, 5656])

    def get_secondary_tst(self):
        return reverse('secondarytst', args=[self.id, 5454])

    def get_cancel(self):
        return reverse('cancel', args=[self.id, 2828])

    def get_etax(self):
        return reverse('etaxpaper', args=[self.id, 8282])

    def get_delivery(self):
        return reverse('delivery', args=[self.id, 6565])

    def get_hfl(self):
        return reverse('hfl', args=[self.id, 6868])

    def get_ler_pic(self):
        return reverse('lersend_pic', args=[self.id, 9898])

    def get_po_vat(self):
        return reverse('po_vat', args=[self.id, 8989])

    def get_etax_done(self):
        return reverse('etax_done', args=[self.id, 2424])

    @property
    def brand_name(self):
        return self.invoices.all()[0].brand if self.invoices.all().count() > 0 else ''

    @property
    def product_name(self):
        return self.invoices.all()[0].product if self.invoices.all().count() > 0 else ''


    @property
    def number_str(self):
        return f'{self.id}_{self.tel_number}'

platform = (
    ('Shopee','Shopee'),
    ('Lazada', 'Lazada'),
    ('Nocnoc','Nocnoc'),
    ('Website&Line&FB','Website&Line&FB'),
    ('Others','Others'),
)


class invoice_product(models.Model):
    name = models.ForeignKey(invoice, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='invoices')
    product = models.ForeignKey(allproduct, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='invoices')
    brand   = models.ForeignKey(Brand,null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='invoices')
    platform = models.CharField(max_length=20, choices=platform, default='', null=True, blank=True)
    qty =  models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    received = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True, help_text="จำนวนเงินที่ได้รับ")
    sell_price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True, help_text="จำนวนเงินที่ออกบิล")
    real_price = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    gp = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
    paymentmade = models.BooleanField(default=False)
    payment_date = models.DateField(blank=True, null=True)
    money_collect = models.BooleanField(default=False)
    collect_date = models.DateField(blank=True, null=True)
    coment_invoice = models.CharField(max_length=10, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(blank=True, null=True,auto_now=True)



    @property
    def invoice_id(self):
        return self.name.id

    @property
    def invoice_name(self):
        return self.name.name
    

    def cost(self):
        return self.real_price*(1-(self.gp/100))

    def total_cost(self):
        if self.real_price and self.qty:
            total_cost = Decimal(str((self.real_price*(1-(self.gp/100)))*self.qty))
            return total_cost.quantize(Decimal('0.01'))
        else:
            return None
    

    def total_receive(self):
        if self.received and self.qty:
            total_receive = Decimal(str(self.received * self.qty))
            return total_receive.quantize(Decimal('0.01'))
        else:
            return None


    @property
    def final_price(self):
        return f'{self.price_eve}:{self.gp}'
# Create your models here.

class ler_delivery(models.Model):
    ler_expected_d = models.ForeignKey(invoice, null=True,blank = True,
            on_delete=models.SET_NULL,
            related_name='deliverys')
    name = models.CharField(max_length=300, null=True, blank=True)