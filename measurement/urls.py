from django.urls import path
from measurement.views import SensorsView, SensorView, SensorCreate, MeasurementCreate

urlpatterns = [
    path('', SensorsView.as_view()),
    path('<pk>/', SensorView.as_view()),
    path('sensor_create/<pk>/', SensorCreate.as_view()),
    path('sensor_create/', SensorCreate.as_view()),
    path('measurement/', MeasurementCreate.as_view()),

]
