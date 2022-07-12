from django.db import models


class Vendor(models.Model):
    manufactured = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.manufactured


class DeviceType(models.Model):
    dev_type = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.dev_type


class Site(models.Model):
    site = models.CharField(max_length=20, unique=True)
    full_name = models.CharField(max_length=20)
    address = models.CharField(max_length=150)

    def __str__(self):
        return self.site


class Device(models.Model):
    site = models.ForeignKey(Site, on_delete=models.PROTECT, null=True)
    name = models.CharField(max_length=10)
    manufactured = models.ForeignKey(Vendor, on_delete=models.PROTECT, null=True)
    dev_type = models.ForeignKey(DeviceType, on_delete=models.PROTECT)
    model_name = models.CharField(max_length=20)
    serial_number = models.CharField(max_length=20)
    description = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.name
