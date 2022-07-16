from django.urls import path

from .device_views import (
    DeviceListView,
    DeviceDetailView,
    DeviceDeleteView,
    DeviceCreateView,
    DeviceUpdateView,
)

from .site_views import (
    SiteListView,
    SiteDetailView,
    SiteDeleteView,
    SiteCreateView,
    SiteDevListView,
    SiteUpdateView,
)

app_name = "netbox"

urlpatterns = [
    path("device/", DeviceListView.as_view(), name="device_list"),
    path("device/create/", DeviceCreateView.as_view(), name="device_create"),
    path("device/detail/<int:pk>/", DeviceDetailView.as_view(), name="device_details"),
    path("device/detail/<int:pk>/delete/", DeviceDeleteView.as_view(), name="device_delete"),
    path("device/detail/<int:pk>/update/", DeviceUpdateView.as_view(), name="device_update"),

    path("site/", SiteListView.as_view(), name="site_list"),
    path("site/create/", SiteCreateView.as_view(), name="site_create"),
    path("site/detail/<int:pk>/", SiteDetailView.as_view(), name="site_details"),
    path("site/detail/<int:pk>/delete/", SiteDeleteView.as_view(), name="site_delete"),
    path("site/detail/<int:pk>/devlist/", SiteDevListView.as_view(), name="site_dev_list"),
    path("site/detail/<int:pk>/update/", SiteUpdateView.as_view(), name="site_update"),
]
