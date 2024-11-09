from django.contrib import admin
from .models import trans
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin




class TrasAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    fields = ('send_date',('mile_start','mile_stop'),'toll_fee','fuel_cost','outsouce_trans',('other_cost','other_cost_remark'),'receive','other_receive','remark')
    list_display = ['send_date','mile_start','mile_stop','mile_sum','remark','created']
    ordering = ('-send_date',)
    search_fields = ['']
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True


admin.site.register(trans, TrasAdmin)


# Register your models here.
