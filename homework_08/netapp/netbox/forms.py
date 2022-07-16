from django.forms import (
    ModelForm,
)


from .models import (
    Device,
    Site,
)

from .baseparams import (
    BaseParamsForm,
)


class DeviceCreateForm(BaseParamsForm, ModelForm):
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


class SiteCreateForm(BaseParamsForm, ModelForm):
    class Meta:
        model = Site
        fields = (
            "site",
            "full_name",
            "address",
        )
