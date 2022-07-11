from django.shortcuts import render, get_object_or_404, Http404
from django.http import HttpRequest
from itertools import chain

from .models import (
    Switch,
    Router,
)


def index(requset: HttpRequest):
    switches = Switch.objects.select_related("manufactured").order_by("name").all()
    routers = Router.objects.select_related("manufactured").order_by("name").all()
    context = {
        "switch": switches,
        "router": routers,
    }

    return render(requset, "netbox/index.html", context=context)


def details(requset: HttpRequest, pk: int):
    switches = Switch.objects.select_related("manufactured").filter(pk=pk)
    routers = Router.objects.select_related("manufactured").filter(pk=pk)
    items = list(chain(switches, routers))[0]
    context = {
        "item": items,
    }
    return render(requset, "netbox/details.html", context=context)
