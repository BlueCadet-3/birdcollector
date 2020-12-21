from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Bird

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def birds_index(request):
  birds = Bird.objects.all()
  return render(request, 'birds/index.html', { 'birds': birds })

def birds_detail(request, bird_id):
  bird = Bird.objects.get(id=bird_id)
  return render(request, 'birds/detail.html', { 'bird': bird })

def assoc_toy(request, bird_id, location_id):
  # Note that you can pass a toy's id instead of the whole object
  Bird.objects.get(id=bird_id).locations.add(location_id)
  return redirect('detail', bird_id=bird_id)

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

class LocationList(ListView):
  model = Location

class LocationDetail(DetailView):
  model = Location

class LocationCreate(CreateView):
  model = Location
  fields = '__all__'

class LocationUpdate(UpdateView):
  model = Location

class LocationDelete(DeleteView):
  model = Location
  success_url = '/locations/'