from django.db import models

# Create your models here.
class Bird(models.Model):
  name = models.CharField(max_length=50)
  kingdom = models.CharField(max_length=50)
  phylum = models.CharField(max_length=50)
  classrank = models.CharField(max_length=50)
  order = models.CharField(max_length=50)
  family = models.CharField(max_length=50)
  genus = models.CharField(max_length=50)
  species = models.CharField(max_length=50)

  def __str__(self):
    return self.name
