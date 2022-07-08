from django.db import models


# Create your models here.
class WeatherList(models.Model):
    temp_min = models.IntegerField()
    temp_max = models.IntegerField()
    temp_main = models.IntegerField()
    type_weather = models.CharField(max_length=50)
    icon = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.city
22