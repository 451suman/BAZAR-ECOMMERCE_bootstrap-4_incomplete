# Generated by Django 5.1.1 on 2024-09-22 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bazar_app', '0003_alter_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='asdasdasdasd'),
        ),
    ]