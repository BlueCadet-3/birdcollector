from django.forms import ModelForm
from .models import Location, Feeding

class FeedingForm(ModelForm):
  class Meta:
    model = Feeding
    fields = ['date', 'meal']

class LocationForm(ModelForm):
  class Meta:
    model = Location
    fields = '__all__'
