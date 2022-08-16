from django.contrib import admin
from .models import Product, Offer

class OfferAdmin(admin.ModeAdmin):
    list_display=('code','discount')


class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','stock')


admin.site.register(Product,ProductAdmin,OfferAdmin)
