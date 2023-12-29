from django.shortcuts import render

from .models import Listing

def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    context = {
        'listing': listing
    }

    return render(request, 'listing_detail.html', context)

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'rental_app/listing_list.html', {'listings': listings})
