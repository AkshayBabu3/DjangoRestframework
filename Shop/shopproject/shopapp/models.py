from django.db import models

# Create your models here.

class products(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.FloatField()
    Discription = models.TextField()
    expiry_date = models.DateField()
    quantity = models.IntegerField(default=0)

class employee(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    mobile = models.CharField(max_length=100,null=True,blank=True)
    place = models.CharField(max_length=100,null=True,blank=True)


class student(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    course = models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100,null=True,blank=True)
    mobile = models.CharField(max_length=100,null=True,blank=True)
    college = models.CharField(max_length=100,null=True,blank=True)
    department = models.CharField(max_length=100,null=True,blank=True)
    university = models.CharField(max_length=100,null=True,blank=True)
