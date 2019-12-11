from django.contrib import admin
from django.db import models
from django.utils.html import format_html

from .models import Car, Seller, Favorite, Product

# def changeToBMW(modeladmin, request, queryset):
#     queryset.update(brand='BMW')
# changeToBMW.short_description = "Change the brand to BMW"

# def changeToMercedes(modeladmin, request, queryset):
#     queryset.update(brand='Mercedes Benz')
# changeToMercedes.short_description = "Change the brand to Mercedes Benz"

class SellerAdmin(admin.ModelAdmin):
     list_display = ('name', 'phone', 'location')

class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'generation', 'year', 'milleageKM', 'url', 'created_at', 'updated_at')
    list_filter = ('brand', 'model')
    search_fields = ('brand','model', 'generation')

class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'description', 'photo', 'show_photo')

    def show_photo(self, obj):
        return format_html('<img src={} style="height:100px;">', obj.photo.url)


# actions = [changeToBMW, changeToMercedes]
# Register your models here.
admin.site.register(Car, CarAdmin)
# admin.site.register(Entry)
# admin.site.register(ProdJSON)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Favorite)
admin.site.register(Product, ProductAdmin)
