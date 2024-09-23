from bazar_app.models import Category, Product, Tag

def navigationFunc(request):
    categories = Category.objects.all()[:7]  # Fetch all categories
    tags = Tag.objects.all()[:7]  # Fetch the first 10 tags
    deals = Product.objects.filter(
        published_at__isnull=False, status="active"
    ).order_by("-published_at")
    
    return {
        "categories": categories,
        "tags": tags,
        "deals": deals,
    }
