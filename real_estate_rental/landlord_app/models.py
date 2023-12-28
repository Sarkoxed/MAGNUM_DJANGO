from django.db import models
from utils_app.models import User


# Create your models here.
class Landlord(User):
    listings = models.ManyToManyRel("rental_app.Listing")
