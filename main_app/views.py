from django.shortcuts import render
from django.http import HttpResponse

# Add temporary fake data
class Bird:
  def __init__(self, name, kingdom, phylum, class, order, family, genus, species):
    self.name = name
    self.kingdom = kingdom
    self.phylum = phylum
    self.class = class
    self.order = order
    self.family = family
    self.genus = genus
    self.species = species

birds = [
  Bird('Eastern barn owl', 'Animalia', 'Chordata', 'Aves', 'Strigiformes', 'Tytonidae', 'Tyto', 'T. javanica'),
  Bird('Common raven', 'Animalia', 'Chordata', 'Aves', 'Passeriformes', 'Corvidae', 'Corvus', 'C. corax'),
  Bird('Common grackle', 'Animalia', 'Chordata', 'Aves', 'Passeriformes', 'Icteridae', 'Quiscalus', 'Q. quiscula'),
]


# Create your views here.
def home(request):
  return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')

def about(request):
  return render(request, 'about.html')

def birds_index(request):
  return render(request, 'birds/index.html', { 'birds': birds })