from django.contrib import admin
from .models import Listing, Review, Favourite, House

admin.site.register(Listing)
admin.site.register(Review)
admin.site.register(Favourite)
admin.site.register(House)

# Register your models here.
