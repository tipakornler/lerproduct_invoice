from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class newproductrelease(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['product_id','product_name','price','link_product','created']
    ordering = ('-created',)
    search_fields = ['product_id','product_name']
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True


admin.site.register(new, newproductrelease)