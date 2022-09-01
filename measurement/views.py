from measurement.models import Sensor
from measurement.serializers import SensorSerializer, SensorsSerializer, MeasurementSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorsSerializer


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorCreate(CreateAPIView):
    serializer_class = SensorSerializer


class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreate(CreateAPIView):
    serializer_class = MeasurementSerializer
