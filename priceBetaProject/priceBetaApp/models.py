from django.db import models
class Product(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    category = models.CharField(max_length = 100)
    image_url = models.CharField(max_length = 250, null=True)
    purchase_link = models.CharField(max_length = 250, null=True)
    brand = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits=100, decimal_places=2)
    rating = models.IntegerField()
    Created_date = models.DateTimeField()
   
