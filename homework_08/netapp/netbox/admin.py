from django.contrib import admin

from .models import (
    Vendor,
    Device,
)


class CommonAdminData(admin.ModelAdmin):
    list_display = (
        "id",
        "dev_type",
        "name",
        "manufactured",
        "model_name",
        "serial_number",
    )
    list_display_links = (
        "id",
        "name",
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related("manufactured")


admin.site.register(Device, CommonAdminData)
admin.site.register(Vendor)
