from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Landlord, Tenant

def home(request):
    return render(request, "home.html")

def list_landlord(request, name):
    listing = Landlord.objects.get(name=name)
    context = {"landlord": listing}
    return render(request, "landlord.html", context)

def list_landlords(request):
    lands = Landlord.objects.all()
    context = {"landlords": lands}
    return render(request, "landlords.html", context)

def list_tenant(request, name):
    listing = Tenant.objects.get(name=name)
    context = {"tenant": listing}
    return render(request, "tenant.html", context)
