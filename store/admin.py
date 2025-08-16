from django.contrib import admin
from .models import Category, Customer, Product , Order, Profile
from django.contrib.auth.models import User

admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Profile)


# Mix Profile info and user info
class ProfileInLine(admin.StackedInline):
    model = Profile

# Extend User model
class UserAdmin(admin.ModelAdmin):
    model = User
    field = ["username","first_name","last_name","email"]
    inlines = [ProfileInLine]

# Unregister the old way
admin.site.unregister(User)


# Re register the new way
admin.site.register(User, UserAdmin)