from django.contrib import admin
from .models import ShippingAddress, Order, OrderItem
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(ShippingAddress)
admin.site.register(Order)
admin.site.register(OrderItem)

# create an OrderItem inline
class OrderItemInLine(admin.StackedInline):
    model = OrderItem
    extra = 0

# Extend or Order models
class OrderAdmin(admin.ModelAdmin):
    model = Order
    readonly_fields = ["date_order"]
    fields = ["user", "full_name", "email", "shipping_address1" , "amount_paid", "date_order", "shipped", "date_shipped"]
    inlines = [OrderItemInLine]


# unregister Order model.
admin.site.unregister(Order)

#Re Register our Order And OrderAdmin.
admin.site.register(Order, OrderAdmin)