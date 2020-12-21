from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('B', 'Breakfast'),
  ('L', 'Lunch'),
  ('D', 'Dinner')
)

# Create your models here.

class Location(models.Model):
  state = models.CharField(max_length=50)
  country = models.CharField(max_length=50)
  continent = models.CharField(max_length=50)

  def __str__(self):
    return f"{self.state}, {self.country}, {self.continent}"
  
  def get_absolute_url(self):
    return reverse('locations_detail', kwargs={'pk': self.id})

class Bird(models.Model):
  name = models.CharField(max_length=50)
  kingdom = models.CharField(max_length=50)
  phylum = models.CharField(max_length=50)
  classrank = models.CharField(max_length=50)
  order = models.CharField(max_length=50)
  family = models.CharField(max_length=50)
  genus = models.CharField(max_length=50)
  species = models.CharField(max_length=50)
  locations = models.ManyToManyField(Location, blank=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('detail', kwargs={'bird_id': self.id})
  
  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)

class Feeding(models.Model):
  date = models.DateField('Feeding Date')
  meal = models.CharField(
    max_length=1,
    choices = MEALS,
    default = MEALS[0][0]
  )
  bird = models.ForeignKey(Bird, on_delete = models.CASCADE)

  class Meta:
    ordering = ['-date']

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"
  