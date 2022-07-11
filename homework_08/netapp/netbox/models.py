from django.db import models


class Vendor(models.Model):
    manufactured = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.manufactured


class Device(models.Model):
    dev_types = [
        ("Router", "Router"),
        ("Switch", "Switch"),
    ]
    name = models.CharField(max_length=10, null=False)
    dev_type = models.CharField(max_length=30, choices=dev_types)
    manufactured = models.ForeignKey(Vendor, on_delete=models.PROTECT, null=True)
    model_name = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name
