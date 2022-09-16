from measurement.models import Sensor
from measurement.serializers import SensorSerializer, SensorsSerializer, MeasurementSerializer
from rest_framework.generics import ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView
from django.shortcuts import get_object_or_404


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class SensorView(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreate(CreateAPIView):
    serializer_class = MeasurementSerializer
    def perform_create(self, serializer):
        sensor = get_object_or_404(Sensor, id=self.request.data.get('sensor'))
        return serializer.save(sensor=sensor)

