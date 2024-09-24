from django import forms
from bazar_app.models import Contact, Product
from django_summernote.widgets import SummernoteWidget


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "content": SummernoteWidget(attrs={"class": "form-control"}),
            "description": SummernoteWidget(attrs={"class": "form-control"}),
        }

