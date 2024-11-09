from django.contrib import admin
from .models import Order, OrderItem, Payment


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'tel', 'email', 'address', 'postal_code','grand_price', 'note', 'paid', 'created',
                    'updated']
    list_filter = ['paid', 'created', 'updated']
    raw_id_fields = ['promocode']
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['payer_name','payer_date']