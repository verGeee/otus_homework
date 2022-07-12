from django.urls import path

from .views import (
    DeviceListView,
    SiteListView,
    SiteDetailView,
    DeviceDetailView,
)

app_name = "netbox"

urlpatterns = [
    path("", DeviceListView.as_view(), name="list"),
    path("detail/<int:pk>/", DeviceDetailView.as_view(), name="details"),
    path("site/", SiteListView.as_view(), name="site_list"),
    path("site/<str:site>/", SiteDetailView.as_view(), name="site"),
]
