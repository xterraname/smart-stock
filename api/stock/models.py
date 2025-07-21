from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class Werehouse(models.Model):
    name = models.CharField(max_length=50, unique=True)

    location = models.PointField(default=Point(72.36100044813004, 40.76964445146663))

    def __str__(self):
        return self.name
