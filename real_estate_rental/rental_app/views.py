from django.shortcuts import render
from .models import Listing, House, Review


def listing_detail(request, title):
    listing = Listing.objects.get(title1=title)
    context = {"listing": listing}
    return render(request, "listing_detail.html", context)


def listing_list(request):
    listings = Listing.objects.all()
    return render(request, "listing_list.html", {"listings": listings})

def reviews(request):
    reviews = Review.objects.all()
    return render(request, "reviews.html", {"reviews": reviews})
