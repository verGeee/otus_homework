from django.contrib import admin

from .models import Switch, Router


class CommonAdminData(admin.ModelAdmin):
    list_display = ("id", 'name', "dev_type", "manufactured", "model_name", "serial_number")
    list_display_links = ("id", 'name', "model_name")


admin.site.register(Switch, CommonAdminData)
admin.site.register(Router, CommonAdminData)
