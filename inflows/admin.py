from django.contrib import admin
from . import models


class InflowsAdmin(admin.ModelAdmin):
    list_display = ('supplier', 'product', 'quantity', 'descripition', 'created_at', 'updated_at')
    search_fields = ('supplier__name', 'product__title')


admin.site.register(models.Inflow, InflowsAdmin)
