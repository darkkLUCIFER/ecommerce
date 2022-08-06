from django.contrib import admin
from .models import Product, ProductGallery


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'active', 'visit_count',)
    list_editable = ('active',)


@admin.register(ProductGallery)
class ProductGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'product',)
