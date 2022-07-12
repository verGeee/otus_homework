from django.shortcuts import (
    get_object_or_404,
)

from django.views.generic import (
    ListView,
    DetailView,
)

from .models import (
    Device,
    Site,
)

from django.db import models

class DeviceListView(ListView):
    queryset = Device.objects.select_related("manufactured").order_by("name")
    context_object_name = "items"


class SiteListView(ListView):
    queryset = Site.objects.order_by("site")
    context_object_name = "items"

class SiteDetailView(ListView):
    queryset = Device.objects
    context_object_name = "items"
    template_name = "netbox/site.html"

    def get_queryset(self):
        qs = super().get_queryset()
        site: Site = get_object_or_404(Site, site=self.kwargs["site"])
        return qs.filter(site__id=site.id)

class DeviceDetailView(DetailView):
    queryset = Device.objects.select_related("site", "manufactured", "dev_type")
    context_object_name = "item"
    template_name = "netbox/details.html"


