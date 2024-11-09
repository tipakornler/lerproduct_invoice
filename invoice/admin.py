from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin





class ProductInvoiceInline(admin.TabularInline):
    model = invoice_product  
    fields = ('product', 'brand', 'platform', 'qty', 'received', 'sell_price', 'real_price', 'gp')
    autocomplete_fields = ['product']  # ใช้ autocomplete field
    readonly_fields = ('created', 'updated')
    extra = 0 
    show_change_link = True
    verbose_name = 'List product'
    verbose_name_plural = 'List product'

class InvoiceAdmin(admin.ModelAdmin):
    inlines = [ProductInvoiceInline]





class InvoiceAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    fields = [('order_number','overall'),('name','tel_number'),'address',('evenote','overall_invoice'),'name_invoce','address_invoice','tax_number','email_addess','brance','invoice_date',('invoice_etax','etax'),'invoice','ler_pickup','ler_note','cancel_inv','cancel_date',('map_pic','receive_pic'),'showroom',('comment','comment2')]
    list_display = ['order_number','name','tax_number','invoice_etax','invoice','count_invoice_number','invoice_tst','brand_name','paid','id','invoice_date','comment','comment2']
    ordering = ('-created',)
    list_editable = ['invoice_etax','invoice','paid','count_invoice_number','invoice_tst']
    search_fields = ['name','order_number','tel_number','count_invoice_number']
    list_filter = ['paid']
    inlines = [ProductInvoiceInline]
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True
    def save_formset(self, request, form, formset, change):
        pre_instance = form.instance
        print(f'Save invoice : {pre_instance.order_number}')
        # 1)Detect platform
        platform        = ''
        invoice_number  =  pre_instance.order_number       
        if invoice_number[0:2] in ['24','25']:
            platform    = 'Shopee'
        if invoice_number[0:3] == 'NN-':
            platform    = 'Nocnoc'
        print(f'Platform is {platform}')
             
        instances = formset.save(commit=False)

        for obj in formset.deleted_objects:
              obj.delete()
        
        for instance in instances: #only new item
            # Do something with instance
            print(f'>{instance.product}')
            # Assign Platform
            instance.platform = platform
            # Get Product from Allproduct model
            p = allproduct.objects.get(productname=instance.product)
            # Get/Assign Brand
            instance.brand = p.brand
            # Get/Assign Real price
            instance.real_price = p.productprice
            # Get/Assign GP
            instance.gp = p.gp
        
            instance.save()
        formset.save_m2m()

admin.site.register(invoice, InvoiceAdmin)



class Invoice_ProductAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['invoice_id','name','brand','invoice_name','paymentmade','payment_date','total_cost','money_collect','collect_date','received','total_receive','product','cost','created',]
    list_editable = ['paymentmade','payment_date','money_collect','received','collect_date']
    list_display_links = ['name']
    list_filter = ['brand','platform','paymentmade','money_collect']
    search_fields = ['product__productname','name__name','name__order_number','name__invoice_eve','name__evenote','name__id']



admin.site.register(invoice_product, Invoice_ProductAdmin)



    # def get_actions(self, request, line_text):
    #     actions = super().get_actions(request)
    #     if request.product():
    #         line_text('product')
    #     return actions
# Register your models here.
