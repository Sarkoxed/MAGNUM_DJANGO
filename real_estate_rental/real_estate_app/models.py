from django.db import models
from utils_app.models import RealEstate


class House(RealEstate):
    bedrooms = models.IntegerField(validators=[models.MinValueValidator(1)])
    floors = models.IntegerField(validators=[models.MinValueValidator(1)])
    bathrooms = models.IntegerField(validators=[models.MinValueValidator(0)])


class Flat(RealEstate):
    bedrooms = models.IntegerField()
    bathrooms = models.IntegerField(
        validators=[models.MinValueValidator(0), models.MaxValueValidator(1)]
    )
    floor_number = models.IntegerField()


class Warehouse(RealEstate):
    area = models.DecimalField(max_digits=8, decimal_places=2)
