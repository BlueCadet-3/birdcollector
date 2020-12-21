from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Bird, Location
from .forms import FeedingForm

# Create your views here.

class BirdCreate(CreateView):
  model = Bird
  fields = '__all__'
  success_url = '/birds/'

class BirdUpdate(UpdateView):
  model = Bird
  fields = '__all__'

class BirdDelete(DeleteView):
  model = Bird
  success_url = '/birds/'

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def birds_index(request):
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
    # Get the toys the cat doesn't have
  locations_bird_doesnt_have = Bird.objects.exclude(id__in = bird.locations.all().values_list('id'))
  # instantiate FeedingForm to be rendered in the template
  feeding_form = FeedingForm()
  return render(request, 'birds/detail.html', {
    # pass the cat and feeding_form as context
    'bird': bird, 'feeding_form': feeding_form,
    # Add the toys to be displayed
    'locations': locations_bird_doesnt_have
  })

def add_feeding(request, bird_id):
	# create the ModelForm using the data in request.POST
  form = FeedingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_feeding = form.save(commit=False)
    new_feeding.bird_id = bird_id
    new_feeding.save()
  return redirect('detail', bird_id=bird_id)

def add_location(request, bird_id):
	# create the ModelForm using the data in request.POST
  form = LocationForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_location = form.save(commit=False)
    new_location.bird_id = bird_id
    new_location.save()
  return redirect('detail', bird_id=bird_id)

def assoc_location(request, bird_id, location_id):
  # Note that you can pass a toy's id instead of the whole object
  Bird.objects.get(id=bird_id).locations.add(location_id)
  return redirect('detail', bird_id=bird_id)

class LocationList(ListView):
  model = Location

class LocationDetail(DetailView):
  model = Location

class LocationCreate(CreateView):
  model = Location
  fields = '__all__'

class LocationUpdate(UpdateView):
  model = Location
  fields = '__all__'

class LocationDelete(DeleteView):
  model = Location
  success_url = '/locations/'