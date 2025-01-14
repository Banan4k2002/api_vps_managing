from django.contrib import admin

from vps.models import VPS


@admin.register(VPS)
class VPSAdmin(admin.ModelAdmin):
    list_display = ('uid', 'cpu', 'ram', 'hdd', 'status')
    list_filter = ('status',)
