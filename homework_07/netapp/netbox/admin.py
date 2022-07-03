from django.contrib import admin

from .models import Switch, Router, Vendor


class CommonAdminData(admin.ModelAdmin):
    list_display = ("id", 'name', "manufactured", "model_name", "serial_number")
    list_display_links = ("id", 'name', "model_name")

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("manufactured")


admin.site.register(Switch, CommonAdminData)
admin.site.register(Router, CommonAdminData)
admin.site.register(Vendor)