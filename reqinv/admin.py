from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.
class ReqinvAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['order_m','name','platform','created','updated']
    ordering = ('-created',)
    search_fields = ['order_m','name']
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True


admin.site.register(reqinv, ReqinvAdmin)
