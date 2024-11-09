from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
class asset_AssetAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['asset_name','company','asset_price','purchase_date']
    search_fields = ['asset_name','company']
    # list_editable = []
    # list_display_links = []

admin.site.register(asset,asset_AssetAdmin,)



# Register your models here.
