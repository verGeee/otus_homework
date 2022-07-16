from django.forms import (
    ModelForm,
)

from .models import (
    Device,
    Site,
)


class DeviceCreateForm(ModelForm):
    class Meta:
        model = Device
        fields = (
            "site",
            "name",
            "manufactured",
            "dev_type",
            "model_name",
            "serial_number",
            "description",
        )


class SiteCreateForm(ModelForm):
    class Meta:
        model = Site
        fields = (
            "site",
            "full_name",
            "address",
        )
