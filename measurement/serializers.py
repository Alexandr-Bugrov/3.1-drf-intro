from rest_framework import serializers
from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date']


class SensorSerializer(serializers.ModelSerializer):
    measurement = MeasurementSerializer
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']