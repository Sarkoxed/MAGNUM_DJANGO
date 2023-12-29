"""
URL configuration for real_estate_rental project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users_app.views import list_landlord, list_landlords, list_tenant, home
from rental_app.views import listing_list, listing_detail

urlpatterns = [
    path("admin/", admin.site.urls),
    path("listings/", listing_list, name="listing_list"),
    path("listings/<str:title>/", listing_detail, name="listing_detail"),
    path("landlords", list_landlords, name="list_landlords"),
    path("landlords/<str:name>", list_landlord, name="list_landlord"),
    path("tenants/<str:name>", list_tenant, name="list_tenant"),
    path("", home, name="home")
]
