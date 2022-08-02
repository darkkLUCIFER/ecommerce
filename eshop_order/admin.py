from django.contrib import admin
from .models import Order, OrderDetail


class OrderDetailInlineAdmin(admin.StackedInline):
    model = OrderDetail
    fields = ('product', 'price', 'count',)
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('owner', 'is_paid', 'payment_date',)
    list_editable = ('is_paid',)
    inlines = (OrderDetailInlineAdmin,)
