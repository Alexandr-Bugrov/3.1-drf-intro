from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)

class Measurement(models.Model):
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now_add=True)
    sensor = models.ForeignKey(Sensor, on_delete=models.PROTECT, related_name='measurement')
