
from django.contrib import admin

from store_app.models import Goods, Categories


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'created_at', 'updated_at']
    list_filter = ['id', 'category', 'created_at','updated_at']
    search_fields = ['category', 'created_at', 'updated_at']
    fields = ['category', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']

class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'good', 'price', 'created_at', 'updated_at']
    list_filter = ['id', 'good', 'category', 'price', 'created_at','updated_at']
    search_fields = ['good', 'price', 'category', 'created_at', 'updated_at']
    fields = ['good', 'price', 'category', 'created_at', 'updated_at', 'pic']
    readonly_fields = ['created_at', 'updated_at']



admin.site.register(Categories, CategoriesAdmin)
admin.site.register(Goods, GoodsAdmin)