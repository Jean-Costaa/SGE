from django.contrib import admin
from . import models


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ('name',)


admin.site.register(models.Category, CategoriesAdmin)
