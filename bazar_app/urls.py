
from django.urls import path

from bazar_app import views

urlpatterns = [
   path("",views.HomeView.as_view(), name="home"),
   path("productdetail/",views.ProductDetailView.as_view(), name="productdetail"),
]
