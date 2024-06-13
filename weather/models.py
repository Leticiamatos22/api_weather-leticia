# models.py
from django.db import models

class WeatherData(models.Model):
    city_name = models.CharField(max_length=100)
    temperature = models.FloatField()

    def __str__(self):
        return f"{self.city_name} - {self.temperature}°C"
