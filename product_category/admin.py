from django.contrib import admin
from .models import ProductCategory


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'active',)
    prepopulated_fields = {'slug': ('title',)}
