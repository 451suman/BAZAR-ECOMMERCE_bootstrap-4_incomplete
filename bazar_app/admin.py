from django.contrib import admin

from bazar_app.models import Category, Product, Tag
from django_summernote.admin import SummernoteModelAdmin

# Register your models here .

admin.site.register([Category, Tag])

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('content',)

admin.site.register(Product, ProductAdmin)