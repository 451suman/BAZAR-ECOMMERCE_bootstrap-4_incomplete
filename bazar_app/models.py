from django.db import models

# Create your models here.
class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Category(TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag (TimeStampModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Product(TimeStampModel):
    STATUS_CHOICES = [
        ("active","Active"),
        ("in_active","Inactive"),
    ]
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="post_images/%Y/%m/%d", blank=False)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="active")
    published_at = models.DateTimeField(null=True, blank =True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title