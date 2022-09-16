from django.urls import path
from measurement.views import SensorsView, SensorView, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorView.as_view()),
    path('measurement_create/', MeasurementCreate.as_view()),

]
