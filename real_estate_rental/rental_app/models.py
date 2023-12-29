from django.db import models
from users_app.models import Landlord, Tenant
from real_estate_app.models import House, Flat, Warehouse
from utils_app.models import RealEstate
from django.core.validators import MinValueValidator, MaxValueValidator

class Listing(models.Model):
    PROPERTY_TYPES = (("house", "HOUSE"), ("flat", "FLAT"), ("warehouse", "WAREHOUSE"))
    property_type = models.CharField(
        max_length=20, choices=PROPERTY_TYPES, default="flat"
    )
    listing_landlord = models.ForeignKey(
        Landlord, on_delete=models.CASCADE
    )
    cur_tenant = models.ForeignKey(
        Tenant, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    def __str__(self):
        return f"Review for {self.listing}"


class Favourite(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tenant} - {self.listing}"