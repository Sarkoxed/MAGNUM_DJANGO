from django.db import models
from rental_app.models import Listing
from utils_app.models import User


# Create your models here.
class Tenant(User):
    leasing_start = models.DateTimeField(auto_now_add=True)
    leasing_end = models.DateTimeField()
    favourites = models.ManyToManyField(Listing, through="Favourite")


class Favourite(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tenant} - {self.listing}"
