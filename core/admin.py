from django.contrib import admin
from core.models import Stamp


class StampAdmin(admin.ModelAdmin):
    pass

admin.site.register(Stamp, StampAdmin)
