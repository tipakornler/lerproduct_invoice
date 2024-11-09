from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin

class InvoiceIssue(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['order_number','topic','user','created','updated']
    ordering = ('-created',)
    # list_editable = ['invoice','paid','count_invoice_number','invoice_tst']
    search_fields = ['order_number','topic']
    autocomplete_fields = ['order_number']
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True


admin.site.register(issue, InvoiceIssue)

# Register your models here.
