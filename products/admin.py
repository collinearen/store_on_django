from django.contrib import admin

from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category',)
    fields = ('name', 'category', 'description', ('price', 'quantity'), 'image',)
    search_fields = ('name',)
    ordering = ('price',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'create_timestamp')
    readonly_fields = ('create_timestamp',)
    extra = 0
