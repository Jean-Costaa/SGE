from django.contrib import admin
from . import models


class AIResutAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'result',)


admin.site.register(models.AIresult, AIResutAdmin)