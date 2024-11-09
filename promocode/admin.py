from django.contrib import admin
from .models import code
# Register your models here.
# @admin.register(code)
class codeAdmin(admin.ModelAdmin):
    list_display = ['name','decription','total','used','discount_rate','discount_price','activated']
    list_filter = ['activated']
    search_fields = ['name']
    save_as = True
    save_as_continue = True
    save_on_top =True
    list_select_related = True
    filter_horizontal = ('brands',)

admin.site.register(code, codeAdmin)