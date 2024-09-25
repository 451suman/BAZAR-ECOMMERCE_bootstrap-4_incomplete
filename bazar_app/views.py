from django.contrib import messages
from winreg import CreateKey
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, TemplateView, View, DetailView, CreateView, DeleteView

from bazar_app.forms import AddProductForm, ContactForm
from bazar_app.models import Category, Contact, Product, Tag
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class SignupView(View):
    template_name = 'registration/signup.html'

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Signup successful! You can now log in.')
            return redirect("login")  # Redirect to login after successful signup
        else:
            messages.error(request, 'Signup Failed!')
            return render(request, self.template_name, {'form': form})  # Re-render form with errors if not valid

    def get(self, request):
        form = UserCreationForm()
        return render(request, self.template_name, {'form': form})
    




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


class ProductsListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"

    def get_queryset(self):
        query = super().get_queryset()
        query = Product.objects.filter(published_at__isnull=False, status="active").order_by("-published_at")
        return query


class ProductsListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        query = Product.objects.filter(published_at__isnull=False, status="active").order_by("-published_at")
        return query


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"

    def get_queryset(self):
        query = super().get_queryset()
        query = Product.objects.filter(published_at__isnull=False, status="active")
        return query


class CategoryListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False,
            status="active",
            category__id=self.kwargs["cid"],
        )
        return query


class TagListView(ListView):
    model = Product
    template_name = "products.html"
    context_object_name = "products"
    paginate_by = 6

    def get_queryset(self):
        query = super().get_queryset()
        query = query.filter(
            published_at__isnull=False,
            status="active",
            tag__id=self.kwargs["tid"],
        )
        return query


class CategoryViewListPage(ListView):
    model = Category
    template_name = "category_Tag_listpage.html"
    context_object_name="categorieslists"

    def get_queryset(self):
        query= super().get_queryset()
        query = Category.objects.all().order_by("name")
        return query
    
class TagViewListPage(ListView):
    model = Tag
    template_name = "category_Tag_listpage.html"
    context_object_name="categorieslists"

    def get_queryset(self):
        query= super().get_queryset()
        query = Tag.objects.all().order_by("name")
        return query
    
class ContactView(TemplateView):
    # model = Contact
    template_name = "contact.html"
    # form_class = ContactForm

    # def get_success_url(self,request):
    #     return render(request, self.template_name)



class AddProduct(LoginRequiredMixin, CreateView):
    model = Product
    template_name = "admin/product_crud/add_products.html"
    form_class = AddProductForm

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Product added successfully!")
        return response
    
    def get_success_url(self):
        return reverse_lazy("productdetail", kwargs={"pk": self.object.pk})
    

class ProductDeleteview(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("product-lists")
    # success_url: This attribute defines the URL to redirect to after the Post has been successfully deleted.

    def form_valid(self, form):
        messages.success(self.request, "product was Deleted Successfully")
        return super().form_valid(form)
