from django.db import models


class WeatherModels(models.Model):
    city = models.CharField(max_length=65)
    temp = models.CharField(max_length=4)
    icon = models.ImageField(null=True)

    class Meta:
        verbose_name_plural = "City"

    def __str__(self):
        return str(self.city)