from django.contrib import admin

from bazar_app.models import Category, Product, Tag, Contact
from django_summernote.admin import SummernoteModelAdmin

# Register your models here .

admin.site.register([Category, Tag, Contact])

class ProductAdmin(SummernoteModelAdmin):
    summernote_fields = ('description')

admin.site.register(Product, ProductAdmin)