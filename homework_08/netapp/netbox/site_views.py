from django.shortcuts import (
    get_object_or_404,
)

from django.urls import (
    reverse_lazy,
    reverse,
)

from django.views.generic import (
    ListView,
    DetailView,
    DeleteView,
    CreateView,
)

from .models import (
    Device,
    Site,
)

from .forms import (
    SiteCreateForm,
)


class BaseParams:
    context_object_name = "items"


class SiteListView(BaseParams, ListView):
    queryset = Site.objects.order_by("site")
    template_name = "netbox/site/site_list.html"


class SiteDetailView(BaseParams, DetailView):
    queryset = Site.objects
    template_name = "netbox/site/site_detail.html"


class SiteDevListView(BaseParams, ListView):
    queryset = Device.objects
    template_name = "netbox/site/site_dev_list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        site: Site = get_object_or_404(
            Site,
            pk=self.kwargs["pk"],
        )
        return qs.filter(site__id=site.id)


class SiteCreateView(BaseParams, CreateView):
    model = Site
    template_name = "netbox/site/site_create.html"

    def get_success_url(self):
        return reverse_lazy("netbox:site_list")

    form_class = SiteCreateForm


class SiteDeleteView(BaseParams, DeleteView):
    model = Site
    success_url = reverse_lazy("netbox:site_list")
    template_name = "netbox/site/site_delete.html"