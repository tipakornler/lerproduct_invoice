from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin


class locationInventoryAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['location']
    list_editable = []
    search_fields = []
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True


admin.site.register(locationInventory, locationInventoryAdmin)


class ProductInventoryAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['product','brand','qty_in','qty_out','qty_sum','status']
    list_filter = ['brand','status']
    autocomplete_fields = ['product']
    ordering = ('-created',)
    list_editable = []
    search_fields = ['product__productname']
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True


admin.site.register(ProductInventory, ProductInventoryAdmin)


class InventoryInAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['productin','location','buy_price','qty','order_number']
    autocomplete_fields = ['productin','order_number']
    ordering = ('-created',)
    search_fields = ['productin__product__productname','order_number__order_number']
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True


admin.site.register(InventoryIn, InventoryInAdmin)

class InventoryOutAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['productout','qty','order_number']
    autocomplete_fields = ['productout','order_number',]
    ordering = ('-created',)
    search_fields = ['productout__product__productname','order_number__order_number']
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True


admin.site.register(InventoryOut, InventoryOutAdmin)