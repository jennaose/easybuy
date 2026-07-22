from django.contrib import admin
from .models import Category, Listing,ListingImage
# Register your models here.

class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'seller', 'category', 'price', 'status', 'created_at']
    list_filter= ['status', 'category']
    search_fields = ['title', 'description']
    inlines = [ListingImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'slug']
    prepopulated_fields = {'slug': ('name',)}

#this can also be written as admin.site.register(Category, CategoryAdmin)