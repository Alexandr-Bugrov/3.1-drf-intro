from django.urls import path
from measurement.views import SensorsView, SensorView, SensorCreate, MeasurementCreate, SensorUpdate

urlpatterns = [
    path('', SensorsView.as_view()),
    path('<pk>/', SensorView.as_view()),
    path('sensor_update/<pk>/', SensorUpdate.as_view()),
    path('sensor_create/', SensorCreate.as_view()),
    path('measurement_create/', MeasurementCreate.as_view()),

]
