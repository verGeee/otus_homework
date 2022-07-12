from django.contrib import admin

from .models import (
    Vendor,
    Device,
    DeviceType,
    Site,
)


class CommonAdminData(admin.ModelAdmin):
    list_display = (
        "id",
        "site",
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


class CommonSiteData(admin.ModelAdmin):
    list_display = (
        "id",
        "site",
        "full_name",
        "address",
    )

    list_display_links = (
        "id",
        "site",
    )


admin.site.register(Device, CommonAdminData)
admin.site.register(Site, CommonSiteData)
admin.site.register(DeviceType)
admin.site.register(Vendor)
