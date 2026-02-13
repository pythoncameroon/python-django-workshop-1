from django.contrib import admin
from .models import Shareholder, Buyer, Share

# Register your models here.

@admin.register(Shareholder)
class ShareholderAdmin(admin.ModelAdmin):

    list_display = ['company_name', 'user', 'created_at']
    search_fields = ['company_name', 'user__username']
    list_filter = ['created_at']
    readonly_fields = ['created_at']

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):

    list_display = ['first_name', 'last_name', 'user', 'balance', 'created_at']
    search_fields = ['first_name', 'last_name', 'user__username']
    list_filter = ['created_at']
    readonly_fields = ['created_at']

@admin.register(Share)
class ShareAdmin(admin.ModelAdmin):
    list_display = ['title', 'shareholder', 'price', 'quantity', 'created_at']
    search_fields = ['title', 'shareholder__company_name',]
    list_filter = ['created_at', 'shareholder']
    readonly_fields = ['created_at', 'updated_at']
    filter_horizontal = ['buyers']