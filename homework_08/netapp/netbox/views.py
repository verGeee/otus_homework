from django.shortcuts import (
    render,
    get_object_or_404,
)
from django.http import HttpRequest
from django.views.generic import (
    ListView,
    FormView,
)


from .models import Device


def index(requset: HttpRequest):
    items = Device.objects.select_related("manufactured").order_by("name").all()
    context = {
        "items": items,
    }

    return render(requset, "netbox/index.html", context=context)


def details(requset: HttpRequest, pk: int):
    items = get_object_or_404(Device.objects.select_related("manufactured"), pk=pk)
    context = {
        "item": items,
    }
    return render(requset, "netbox/details.html", context=context)


class DeviceListView(ListView):
    queryset = Device.objects.select_related("manufactured")
    context_object_name = "items"
