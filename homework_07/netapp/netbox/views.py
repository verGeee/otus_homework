from django.shortcuts import render, HttpResponse, get_object_or_404
from django.http import HttpRequest

from .models import (
    Switch,
    Router,
)


def index(requset: HttpRequest):
    switches = Switch.objects.order_by("name").all()
    routers = Router.objects.order_by("name").all()
    context = {
        "switch": switches,
        "router": routers,
    }

    return render(requset, "netbox/index.html", context=context)


def details(requset: HttpRequest, pk: int):
    try:
        items = get_object_or_404(Switch, pk=pk)
    except:
        items = get_object_or_404(Router, pk=pk)
    context = {
        "item": items,
    }
    return render(requset, "netbox/details.html", context=context)
