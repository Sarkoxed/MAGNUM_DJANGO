from django.db import models
from landlord_app.models import Landlord
from real_estate_app.models import House, Flat, Warehouse
from utils_app.models import RealEstate


def default_landlord():
    landlord, _ = Landlord.objects.get_or_create(name="Default Landlord")
    return landlord


# Create your models here.
class Listing(models.Model):
    PROPERTY_TYPES = (("house", "HOUSE"), ("flat", "FLAT"), ("warehouse", "WAREHOUSE"))
    property_type = models.CharField(
        max_length=20, choices=PROPERTY_TYPES, default="flat"
    )
    landlord = models.ForeignKey(
        Landlord, related_name="listings", on_delete=models.CASCADE
    )
    cur_tenant = models.ForeignKey(
        "tenant_app.Tenant", on_delete=models.SET_NULL, null=True, blank=True
    )

    def __str__(self):
        return self.title


class Review(models.Model):
    rating = models.IntegerField(
        validators=[models.MinValueValidator(1), models.MaxValueValidator(5)]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    tenant = models.ForeignKey("tenant_app.Tenant", on_delete=models.CASCADE)

    def __str__(self):
        return f"Review for {self.listing}"
