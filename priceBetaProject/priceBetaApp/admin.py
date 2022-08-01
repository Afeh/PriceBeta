from unicodedata import name
from django.contrib import admin

# Register your models here.
from .models import Category, Store, Wishlist, Product

admin.site.register(Category)
# Adding some additional information about the Category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'description']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product)
# Adding some additional information about the Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug', 'price', 'in_stock', 'brand', 'created_at', 'modified_at']
    list_filter = ['in_stock']
    list_editable = ['price', 'in_stock']
    prepopulated_fields = ['slug', ['name']]


admin.site.register(Store)
# Adding some additional information about the Store model
class StoreAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'slug']
    prepopulated_fields = ['slug', ['name']]


admin.site.register(Wishlist)
# Adding some additional information about the Wishlist model
class WishlistAdmin(admin.ModelAdmin):
    list_display = ['wishlist_name', 'user', 'item', 'slug']
    prepopulated_fields = ['slug', ['name']]