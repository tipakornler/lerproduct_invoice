from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class stockInvoiceInline(admin.TabularInline):
    model = stockout
    fields = ('order_number_out','sell_price','qty_out')
    autocomplete_fields = ['order_number_out']
    readonly_fields = ('created','updated')
    extra = 0 
    show_change_link = True
    verbose_name = 'List product'
    verbose_name_plural = 'List product'

class InvoiceInline(admin.ModelAdmin):
	inlines =[stockInvoiceInline]

class stock_ProductAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['order_number','product','qty','qtyout','created',]
    search_fields = ['product__productname','order_number__order_number']
    autocomplete_fields = ['product','order_number']
    inlines = [stockInvoiceInline]
    # list_editable = []
    # list_display_links = []

admin.site.register(stockOnhand,stock_ProductAdmin,)








# Register your models here.
