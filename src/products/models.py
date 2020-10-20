from django.db import models
from django.urls import reverse

# Create your models here.

# Let's say I want to create a product.
# The backend (db) needs to know what
# kind of product I've created.


class Product(models.Model):
    # various attributes that a Product should have
    # mapping to database
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    summary = models.TextField(default="This is a new product")
    featured = models.BooleanField(default=True)

    def get_absolute_url(self):
        # this will dynamically get the absolute path to the product detail page
        # you can change the paths in urls.py and everything will get updated
        # return f"/products/{self.id}"
        return reverse("products:product-detail", kwargs={"id": self.id})