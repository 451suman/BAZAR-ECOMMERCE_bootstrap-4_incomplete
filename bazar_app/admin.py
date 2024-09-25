from django.utils.html import format_html
from django.contrib import admin

from bazar_app.models import Category, Product, Tag, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here .

admin.site.register([Category, Tag])


class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = "description"
    list_display = (
        "title",
        "category",
        "price",
        "stock",
        "status",
        "published_at",
        "featured_image_tag",
    )
    list_filter = ("status", "category", "published_at")
    search_fields = ("title", "category__name", "tag__name")
    ordering = ("-published_at",)
    list_per_page = 3

    def featured_image_tag(self, obj):
        if obj.featured_image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px;" />'.format(
                    obj.featured_image.url
                )
            )
        return "No Image"

    featured_image_tag.short_description = "Image Preview"


admin.site.register(Product, ProductAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "message")
    ordering = ("-created_at",)

admin.site.register(Contact, ContactAdmin)
