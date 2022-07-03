from django.db import models


class Vendor(models.Model):
    manufactured = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.manufactured


class CommonData(models.Model):
    name = models.CharField(max_length=10, null=False, default="-")
    manufactured = models.ForeignKey(Vendor, on_delete=models.PROTECT, null=True)
    model_name = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.model_name


class Switch(CommonData):
    dev_type = "Switch"
    port_count = models.IntegerField(default="0")


class Router(CommonData):
    dev_type = "Router"
    prefix_count = models.IntegerField(default="0")
