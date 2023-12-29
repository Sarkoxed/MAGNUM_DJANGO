from django.db import models
from utils_app.models import RealEstate
from django.core.validators import MinValueValidator, MaxValueValidator


class House(RealEstate):
    bedrooms = models.IntegerField(validators=[MinValueValidator(1)])
    floors = models.IntegerField(validators=[MinValueValidator(1)])
    bathrooms = models.IntegerField(validators=[MinValueValidator(0)])


class Flat(RealEstate):
    bedrooms = models.IntegerField()
    bathroom = models.BooleanField()
    floor_number = models.IntegerField()

class Warehouse(RealEstate):
    area = models.DecimalField(max_digits=8, decimal_places=2)
