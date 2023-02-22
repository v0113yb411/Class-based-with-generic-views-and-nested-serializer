from django.contrib import admin
from .models import Category,Products

# Register your models here.

admin.site.register(Category)
admin.site.register(Products)


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=['id','title','created_at','updated_at']
