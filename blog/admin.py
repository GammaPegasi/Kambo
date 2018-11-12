from django.contrib import admin
from .models import Car, Seller, Favorite

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
    # actions = [changeToBMW, changeToMercedes]


# Register your models here.
admin.site.register(Car, CarAdmin)
# admin.site.register(Entry)
# admin.site.register(ProdJSON)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Favorite)

