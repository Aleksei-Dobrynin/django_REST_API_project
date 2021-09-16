from django.db import models
from django.db.models.aggregates import Count
from django.db.models.deletion import CASCADE, SET_NULL

# Create your models here.
class Store(models.Model):
    Name = models.CharField(max_length=30)
    location = models.TextField(null=True,blank=True)


    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=100)
    Description = models.TextField(null=True,blank=True)
    Manufacturer = models.CharField(max_length=50, null=True,blank=True)

    def __str__(self):
        return self.Name

class StoreContent(models.Model):
    Store = models.ForeignKey(Store, on_delete=CASCADE)
    Product = models.ForeignKey(Product, on_delete=SET_NULL,null=True)
    Count = models.IntegerField()

    def __str__(self):
        return str(self.Store.Name) + " " + str(self.Product.Name)
###########################################################################################

class StoreAddProduct(models.Model):
    Store = models.ForeignKey(Store, on_delete=CASCADE)
    Product = models.ForeignKey(Product, on_delete=SET_NULL,null=True)
    Count = models.IntegerField()
    date = models.DateField(auto_now = True)

class StoreBuyProduct(models.Model):
    Store = models.ForeignKey(Store, on_delete=CASCADE)
    Product = models.ForeignKey(Product, on_delete=SET_NULL,null=True)
    Count = models.IntegerField()
    date = models.DateField(auto_now = True)


