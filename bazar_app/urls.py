
from django.urls import path

from bazar_app import views

urlpatterns = [
   path("",views.HomeView.as_view(), name="home"),
   path("productdetail/<int:pk>/",views.ProductDetailView.as_view(), name="productdetail"),
   path("product-lists/",views.ProductsListView.as_view(), name="product-lists"),
   path("product-by-category/<int:cid>/",views.CategoryListView.as_view(), name="product-by-category"),
   path("product-by-tag/<int:tid>/",views.TagListView.as_view(), name="product-by-tag"),
   path("all-categories/",views.CategoryViewListPage.as_view(), name="all-categories"),
   path("all-tags/",views.TagViewListPage.as_view(), name="all-tags"),
]
