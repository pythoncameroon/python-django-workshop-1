from django.contrib import admin
from .models import Shareholder, Buyer, Share, Purchase

class PurchaseInline(admin.TabularInline):
    model = Purchase
    extra = 0  
    readonly_fields = ['purchased_at'] 

@admin.register(Shareholder)
class ShareholderAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'user', 'created_at')
    search_fields = ('company_name', 'user__username')
    list_filter = ('created_at',)

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'user', 'created_at')
    search_fields = ('first_name', 'last_name', 'user__username')
    inlines = [PurchaseInline]

    def full_name(self, obj):
        return f"{obj.first_name} {obj.last_name}"
    full_name.short_description = "Nom complet"

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ('title', 'shareholder', 'price', 'quantity', 'get_total_sold', 'get_remaining')
    list_filter = ('shareholder', 'created_at')
    search_fields = ('title', 'shareholder__company_name')
    inlines = [PurchaseInline]

    def get_total_sold(self, obj):
        return obj.total_sold
    get_total_sold.short_description = "Vendus"

    def get_remaining(self, obj):
        return obj.remaining_quantity()
    get_remaining.short_description = "Restants"

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('buyer', 'share', 'quantity', 'purchased_at')
    list_filter = ('purchased_at', 'share__shareholder')
    search_fields = ('buyer__last_name', 'share__title')
    date_hierarchy = 'purchased_at'