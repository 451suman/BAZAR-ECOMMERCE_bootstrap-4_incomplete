from django.shortcuts import render
from django.views.generic import ListView, TemplateView, View, DetailView

from bazar_app.models import Product


# Create your views here.
class HomeView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products" 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["banners"] = Product.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")[:3]
        context["products"] = Product.objects.filter(
            published_at__isnull=False, status="active"
        ).order_by("-published_at")


        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(published_at__isnull=False, status="active")
        return query