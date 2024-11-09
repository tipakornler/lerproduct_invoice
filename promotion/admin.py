from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin
from import_export import fields, resources
from import_export.widgets import ForeignKeyWidget
from import_export.fields import Field

class BookingResource(resources.ModelResource):
    class Meta:
        model = listpromo
        import_id_fields = ()
        skip_unchanged = True
        report_skipped= True
        fields = ('brandid','normal_price','promotion_price','start_date','end_date')
        exclude = ('id')
        
# class BookingResource(resources.ModelResource):
    # brandid = Field(attribute='allproduct', column_name='brandproductid')
    # class Meta:
    #     model = listptomo
        # import_id_fields = ('brandid__brandproductid')
        # import_id_fields = ()
        # skip_unchanged = True
        # report_skipped= True
        # fields = ('brandid','normal_price','promotion_price','start_date','end_date')
        # exclude = ('id')

# class BookResource(resources.ModelResource):
#     product = fields.Field(
#         column_name='allproduct',
#         attribute='allproduct',
#         widget=ForeignKeyWidget(allproduct, field='brandproductid'))

#     class Meta:
#         model = listptomo
#         fields = ('product',)


@admin.register(listpromo)
class PromotionAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['brandid','normal_price','promotion_price','start_date','end_date']
    ordering = ('-created',)
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True

    fieldsets = [
        ('Basic Information',{'fields': ['brandid','normal_price','promotion_price','start_date','end_date']}),
        ('System Information',{'fields':[]})
        ]
    resource_class = BookingResource




# Register your models here.
