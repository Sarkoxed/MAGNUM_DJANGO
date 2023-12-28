from django.shortcuts import render
from .models import Listing

# Create your views here.
def listing_list(request):
    listings = Listing.objects.all()
    return render(request, "rental_app/listing_list.html", {"listings": listings})

