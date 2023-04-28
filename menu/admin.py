from django.contrib import admin
from .models import MenuItem


class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 0


class MenuItemAdmin(admin.ModelAdmin):
    fields = ['name', 'parent', 'url']  # TODO: Remove "url" after finishing the project
    list_display = ['name', 'url']
    readonly_fields = ('url',)
    ordering = ('url',)
    inlines = [MenuItemInline]


admin.site.register(MenuItem, MenuItemAdmin)
