from django.contrib import admin
from measurement.models import Measurement, Sensor

class SensorMeasurement(admin.TabularInline):
    model = Measurement

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    pass


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    inlines = [SensorMeasurement]

