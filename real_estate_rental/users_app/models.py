from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, default=0.0
    )

    def __str__(self):
        return self.name


class Landlord(User):
    own_listings = models.ManyToManyField("rental_app.Listing", blank=True)


class Tenant(User):
    leasing_start = models.DateTimeField(auto_now_add=True)
    leasing_end = models.DateTimeField()
    favourites = models.ManyToManyField(
        "rental_app.Listing", through="rental_app.Favourite"
    )
