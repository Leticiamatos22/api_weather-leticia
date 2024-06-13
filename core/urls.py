# urls.py
from django.urls import path
from weather.views import WeatherDataListCreate, WeatherDataRetrieveUpdateDestroy

urlpatterns = [
    path('weather/', WeatherDataListCreate.as_view(), name='weather-list-create'),
    path('weather/<int:pk>/', WeatherDataRetrieveUpdateDestroy.as_view(), name='weather-detail'),
]
