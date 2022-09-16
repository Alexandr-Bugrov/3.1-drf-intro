from rest_framework import serializers
from measurement.models import Measurement, Sensor


class MeasurementSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['id', 'temperature', 'date']


class SensorSerializer(serializers.ModelSerializer):
    measurement = MeasurementSensorSerializer
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurement']


class SensorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']

class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['temperature', 'date', 'sensor']
