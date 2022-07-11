from django.urls import path

from .views import (
    index,
    details,
)

app_name = "netbox"

urlpatterns = [
    path("", index, name="list"),
    path("<int:pk>/", details, name="details"),
]
