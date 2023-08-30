from django.db import models
from django.utils import timezone

# Create your models here.

class City(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self) -> str:
    return self.name


class Property(models.Model):
  PURPOSES = [
    ("Sale", "Sale"),
    ("Rent", "Rent"),
  ]

  TYPES = [
    ("House", "House"),
    ("Villa", "Villa"),
    ("Apartment", "Apartment"),
    ("Office", "Office"),
    ("Land", "Land"),
    ("Shop", "Shop"),
    ("Market", "Market"),
    ("Building", "Building"),
    ("Farm", "Farm"),
  ]

  title = models.CharField(max_length=255)
  date = models.DateTimeField(default=timezone.now)
  city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, blank=True)
  neighborhood_or_project = models.CharField(max_length=35, null=True)
  price = models.CharField(max_length=10, null=True)
  purpose = models.CharField(max_length=10, choices=PURPOSES, default="Sale")
  type = models.CharField(max_length=35, choices=TYPES, default="House")
  area = models.IntegerField(null=True)
  bedrooms = models.IntegerField(null=True, blank=True)
  reception_rooms = models.IntegerField(null=True, blank=True)
  bathrooms = models.IntegerField(null=True, blank=True)
  furnishing = models.BooleanField(default=False)
  garden = models.BooleanField(default=False)
  featured = models.BooleanField(default=False)
  main_image = models.ImageField(upload_to="images", null=True)


  def __str__(self) -> str:
    return self.title


class PropertyImage(models.Model):
  property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="image")
  image = models.ImageField(upload_to="images", null=True)

  def __str__(self) -> str:
    return f"{self.property.title} image"