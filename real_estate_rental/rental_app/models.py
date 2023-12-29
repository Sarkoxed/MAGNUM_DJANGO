from django.db import models
from users_app.models import Landlord, Tenant
from django.core.validators import MinValueValidator, MaxValueValidator


class Listing(models.Model):
    title1 = models.CharField(max_length=10, default="aboba")
    PROPERTY_TYPES = (("house", "HOUSE"), ("flat", "FLAT"), ("warehouse", "WAREHOUSE"))
    property_type = models.CharField(
        max_length=20, choices=PROPERTY_TYPES, default="flat"
    )
    property = models.ForeignKey(
        "House", on_delete=models.CASCADE, null=True, blank=True
    )
    listing_landlord = models.ForeignKey(Landlord, on_delete=models.CASCADE)
    cur_tenant = models.ForeignKey(
        Tenant, on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.property.title


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


class House(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
#    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
#    square_feet = models.IntegerField()
    is_free = models.BooleanField()
    bedrooms = models.IntegerField(validators=[MinValueValidator(1)])
    floors = models.IntegerField(validators=[MinValueValidator(1)])
    bathrooms = models.IntegerField(validators=[MinValueValidator(0)])
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
