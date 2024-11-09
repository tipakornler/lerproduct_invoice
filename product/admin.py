from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin


class DiscountAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Discount, DiscountAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ['brand_name']

admin.site.register(Brand, BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug','priority']
    prepopulated_fields = {'slug': ('name',)}




class ProductImageInline(admin.TabularInline):
	model = ProductImage
	fields = ('file','note','link','updated')
	readonly_fields = ('created','updated')
	extra = 0 
	show_change_link = True
	verbose_name = 'Image detail'
	verbose_name_plural = 'Image detail'

class ProductInline(admin.ModelAdmin):
	inlines =[ProductImageInline]



admin.site.register(Category, CategoryAdmin)

		
admin.site.register(ContactForm)
# Register your models here.


class ShopeeAdminFilter(admin.SimpleListFilter):
    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return allproduct.objects.filter(shopee__isnull=False)
        elif value == 'No':
            return allproduct.objects.filter(shopee__isnull=True)
        return queryset
class shopeeBlankFilter(ShopeeAdminFilter):
    title = 'shopee'
    parameter_name = 'shopee'


class LazadaAdminFilter(admin.SimpleListFilter):
    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )
    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return allproduct.objects.filter(lazada__isnull=False)
        elif value == 'No':
            return allproduct.objects.filter(lazada__isnull=True)
        return queryset
class lazadaBlankFilter(LazadaAdminFilter):
    title = 'lazada'
    parameter_name = 'lazada'


@admin.register(allproduct)
class AllproductAdmin(ImportExportModelAdmin,ImportExportActionModelAdmin,admin.ModelAdmin):
    list_display = ['id','productname','productprice','gp','status','brand']
    list_editable = ['status','productprice','gp','brand']
    list_filter = ['brand','category',shopeeBlankFilter,lazadaBlankFilter]
    search_fields = ['productname']
    inlines = [ProductImageInline]
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True

    

# class AllProductAdmin(admin.ModelAdmin):
#     list_display = ['id','productname','productprice','gp','status','brand']
#     list_editable = ['status','productprice','gp','brand']
#     search_fields = ['productname']
#     def get_search_results(self, request, queryset, search_term):
#         # Added on Nov 4,2024 --To fix error if running on WSGI server (gunicorn)
#         if not search_term:
#             return queryset, False
#         # ---------------------------------------------------------------
        
#         print(request.path)
#         if 'autocomplete' in  request.path :
#             print(f"In get search results (autocomplete) : {search_term}")
#             queryset = queryset.exclude(status=False)
#         results = super().get_search_results(request, queryset, search_term)
#         return results

