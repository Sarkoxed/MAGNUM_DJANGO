from django.db import models
from utils_app.models import User

class Landlord(User):
    own_listings = models.ManyToManyField("rental_app.Listing")

class Tenant(User):
    leasing_start = models.DateTimeField(auto_now_add=True)
    leasing_end = models.DateTimeField()
    favourites = models.ManyToManyField("rental_app.Listing", through="rental_app.Favourite")