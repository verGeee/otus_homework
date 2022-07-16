from django import forms


class BaseParamsView:
    context_object_name = "items"


class BaseParamsForm:
    def __init__(self, *args, **kwargs):
        super(BaseParamsForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            if field.widget.__class__ == forms.widgets.Select:
                field.widget.attrs.update(
                    {
                        "class": "form-select",
                        "style": "width: 400px",
                    }
                )
            else:
                field.widget.attrs.update(
                    {
                        "class": "form-control",
                        "style": "width: 400px",
                    }
                )
