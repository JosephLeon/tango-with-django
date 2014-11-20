from django.contrib import admin
from rango.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    prepopulate_fields = {'slug': ('name',)}

admin.site.register(Category)
admin.site.register(Page)
