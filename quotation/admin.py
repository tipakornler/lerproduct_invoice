from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin



class ProductQuotationInline(admin.TabularInline):
    model = quotation_product
    fields = ('product','brand','qty','sell_price')
    autocomplete_fields = ['product']
    readonly_fields = ('created','updated')
    extra = 0 
    show_change_link = True
    verbose_name = 'List product'
    verbose_name_plural = 'List product'

class QuotationInline(admin.ModelAdmin):
	inlines =[ProductQuotationInline]



class QuotationAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['name','tel_number','quotation_date']
    ordering = ('-created',)
    search_fields = ['name']
    inlines = [ProductQuotationInline]
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True


admin.site.register(quotation, QuotationAdmin)



class Quotation_ProductAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['name','created']
    list_display_links = ['name']
    search_fields = ['product']


admin.site.register(quotation_product, Quotation_ProductAdmin)



    # def get_actions(self, request, line_text):
    #     actions = super().get_actions(request)
    #     if request.product():
    #         line_text('product')
    #     return actions
# Register your models here.
