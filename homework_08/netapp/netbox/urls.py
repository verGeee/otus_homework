from django.urls import path

from .views import (
    details,
    DeviceListView,
)

app_name = "netbox"

urlpatterns = [
    path("", DeviceListView.as_view(), name="list"),
    path("<int:pk>/", details, name="details"),
]
