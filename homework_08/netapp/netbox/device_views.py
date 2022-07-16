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
)

from .forms import (
    DeviceCreateForm,
)

from .baseparams import (
    BaseParamsView,
)


class DeviceListView(BaseParamsView, ListView):
    queryset = Device.objects.select_related("manufactured").order_by("name")
    template_name = "netbox/device/device_list.html"


class DeviceDetailView(BaseParamsView, DetailView):
    queryset = Device.objects.select_related("site", "manufactured", "dev_type")
    template_name = "netbox/device/device_detail.html"


class DeviceCreateView(CreateView):
    model = Device
    template_name = "netbox/device/device_create.html"

    def get_success_url(self):
        return reverse("netbox:device_details", kwargs={"pk": self.object.pk})

    form_class = DeviceCreateForm


class DeviceDeleteView(BaseParamsView, DeleteView):
    model = Device
    success_url = reverse_lazy("netbox:device_list")
    template_name = "netbox/device/device_delete.html"
