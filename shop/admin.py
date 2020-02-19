from django.contrib import admin
from django.utils.datetime_safe import datetime
from .models import Product, Purchase, Comment, CustomPurchase

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'product', 'body', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'email', 'body')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'product_type', 'price')
    list_filter = ('name', 'product_type', 'price')
    search_fields = ('name', 'product_type', 'price')
    ordering = ('product_type', 'name', 'price')

@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'product','count', 'status')
    list_filter = ('customer', 'status')
    ordering = ('-status', 'customer')

@admin.register(CustomPurchase)
class CustomPurchaseAdmin(admin.ModelAdmin):
    list_display = ('customer', 'size', 'status')
    list_filter = ('customer', 'status')
    ordering = ('-status', 'customer')
# admin.site.register(Like)


# @admin.register(Like)
# class PurchaseAdmin(admin.ModelAdmin):
#     list_display = ('customer', 'product','like')
#     list_filter = ('customer', 'product')
#     ordering = ('customer',)

