from django.db import models

# Create your models here.
class First_Model(models.Model):
    First_Name=models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Address = models.CharField(max_length=20)
    Contact = models.PositiveIntegerField()
    EmailId = models.EmailField()

    def __str__(self):
        return self.EmailId

class Customer(models.Model):
    name = models.CharField(max_length=128)
    c_id = models.PositiveIntegerField(primary_key=True)
    city_id = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="Id")
    Address = models.CharField(max_length=20)
    Contact = models.PositiveIntegerField()
    EmailId = models.EmailField()
    date_joined = models.DateField()

class City(models.Model):
    Id = models.PositiveIntegerField(primary_key=True)
    city_name = models.CharField(max_length=20)
    zipcode = models.CharField(max_length=20)

class Restaurants(models.Model):
    res_id = models.PositiveIntegerField(primary_key=True)
    res_address = models.CharField(max_length=20)
    c_id = models.ForeignKey(City,on_delete=models.CASCADE,verbose_name="Id")

