from django.contrib import admin
from django.urls import path
from soilMoisture.views import (
    thingspeak_data_temperature,
    thingspeak_data_humidity,
    thingspeak_data_soil_moisture,
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',thingspeak_data_temperature,name='thingspeak_temperature'),
    path('humidity/',thingspeak_data_humidity,name='thingspeak_humidity'),
    path('soil_moisture/',thingspeak_data_soil_moisture,name='thingspeak_soil_moisture'),
]
