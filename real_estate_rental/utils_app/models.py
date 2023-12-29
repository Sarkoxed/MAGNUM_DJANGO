from django.db import models


class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone_number = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)
    rating = models.DecimalField(
        max_digits=2, decimal_places=1, null=True, blank=True, default=0.0
    )

    def __str__(self):
        return self.name


class RealEstate(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    address = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=30, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True)
    square_feet = models.IntegerField()
    is_free = models.BooleanField()

    def __str__(self):
        return self.title
