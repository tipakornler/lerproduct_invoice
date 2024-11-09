from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.

def brand_img(instance, filename):
	return 'files/brand/%s/%s' % (instance.brand_name, filename)


class Brand(models.Model):
	brand_name = models.CharField(max_length=150, db_index=True)
	brand_pic = models.ImageField(upload_to=brand_img, max_length=500)
	def __str__(self):
		return self.brand_name

class Category(models.Model):
	name = models.CharField(max_length=150, db_index=True)
	slug = models.SlugField(max_length=150, unique=True ,db_index=True)
	priority = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('name', )
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('product_list_by_category', args=[self.slug])



class allproduct(models.Model):
	category = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE)
	brand = models.ForeignKey(Brand, related_name='brands', on_delete=models.CASCADE)
	productname = models.CharField(max_length=150, db_index=True)
	productid = models.SlugField(max_length=100, db_index=True)
	brandproductid = models.CharField(max_length=150, null=True, blank=True)
	fakeprice = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
	productprice = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True)
	gp = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
	productdetail = RichTextField(null=True, blank=True)
	promotion = models.BooleanField(default=False)
	promotiontime = models.DateField(null=True, blank=True)
	lazada = models.CharField(max_length=500,blank=True, null=True)
	shopee = models.CharField(max_length=500,blank=True, null=True)
	nocnoc = models.CharField(max_length=500,blank=True, null=True)
	status 	= models.BooleanField(default=True)
	delay_delivery 	= models.BooleanField(default=False)
	askbefore = models.BooleanField(default=False)
	youtube = models.CharField(max_length=500,blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	upload = models.FileField(upload_to='manual/',null=True, blank=True)


	@property
	def sale_price(self):
		# PROMO code
		sale_price = self.productprice
		from .models import Discount
		discount = Discount.objects.filter(activated=True)[0:1]
		if discount:
			sale_price = self.productprice * (100-discount[0].discount_rate)/100 if discount[0].discount_rate else self.productprice - discount[0].discount_price
		# --------
		#  
		return sale_price


	class Meta:
		ordering = ('productname', )
		index_together = (('id', 'productid'),)

	def __str__(self):
		return self.productname

	def get_absolute_url(self):
		return reverse('productdetail', args=[self.id, self.productid])

class Discount(models.Model):
	name 			= models.CharField(max_length=150, primary_key=True)
	description 	= models.TextField()
	discount_rate 	= models.DecimalField(default=0,max_digits=10, decimal_places=2,null=True, blank=True)#%
	discount_price 	= models.DecimalField(default=0,max_digits=10, decimal_places=2,null=True, blank=True)#Price
	start 			= models.DateField(null=True, blank=True)
	stop 			= models.DateField(null=True, blank=True)
	activated 		= models.BooleanField(default=False)
	def __str__(self):
		return f'{self.name}'

class ContactForm(models.Model):
	contact_name = models.CharField(max_length=100)
	contact_email = models.EmailField(max_length=254)
	tel = models.CharField(max_length=60,null=True, blank=True)
	contact_message = models.TextField(null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return 'ContactForm {}'.format(self.contact_name)

def product_img(instance, filename):
	return 'files/product/%s/%s' % (instance.id, filename)

class ProductImage(models.Model):
	product		= models.ForeignKey(allproduct,
							blank=True,null=True,
							on_delete=models.SET_NULL,
							related_name = 'images')
	note			= models.CharField(max_length=150,blank=True, null=True)
	link			= models.CharField(max_length=150,blank=True, null=True)
	file 			= models.ImageField(upload_to=product_img, max_length=500)
	created		 	= models.DateTimeField(auto_now_add=True)
	updated     	= models.DateTimeField(blank=True, null=True,auto_now=True)

	def __str__(self):
		return '%s' % self.product

	def get_image_url(self):
		return self.file.url