from django.contrib import admin

from catalog.models import Product, Category


# admin.site.register(Product)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'purchase_price', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'purchase_price',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')