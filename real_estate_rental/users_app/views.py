from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class TenantView(LoginRequiredMixin, TemplateView):
    template_name = "tenant.html"

    def get_conext_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["data"] = "This is only visible to Tenant"
        return context
    
class LandlordView(LoginRequiredMixin, TemplateView):
    template_name = "landlord.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add landlord-specific context data here
        context['data'] = 'This is only visible to Landlord'
        return context
