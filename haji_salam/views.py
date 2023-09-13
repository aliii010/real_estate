from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import Property, PropertyImage

# Create your views here.

def home(request):
  featured_properties = Property.objects.filter(featured=True).order_by("-date")
  return render(request, "haji_salam/home.html", {
    'featured_properties': featured_properties,
  })

class allProperties(ListView):
  template_name = 'haji_salam/all-properties.html'
  model = Property
  ordering = ["-date"]
  context_object_name = "all_properties"


class PropertyDetail(View):
  def get(self, request, slug):
    identified_prop = Property.objects.get(prop_slug=slug)
    images = PropertyImage.objects.filter(property=identified_prop)

    context = {
      "prop": identified_prop,
      "images": images,
      "city_choices": Property.CITIES,
      "regions_choices": Property.REGIONS,
      "project_choices": Property.PROJECTS,
      "purpose_choices": Property.PURPOSES,
      "type_choices": Property.TYPES,
    }
    return render(request, "haji_salam/prop-detail.html", context)
  

def filterProperty(request):
  if request.method == "POST":
    filtered_properties = Property.objects.all()
    entered_city = request.POST['city'].lower()
    entered_region = request.POST['region']
    entered_project = request.POST['project']
    entered_purpose = request.POST['purpose']
    entered_type = request.POST['type']
    
    if entered_purpose != '' and entered_purpose is not None:
      filtered_properties = filtered_properties.filter(purpose=entered_purpose)

    if entered_type != '' and entered_type is not None:
      filtered_properties = filtered_properties.filter(type=entered_type)
    
    if entered_city != '' and entered_city is not None:
      filtered_properties = filtered_properties.filter(city=entered_city)

    if entered_region != '' and entered_region is not None:
      filtered_properties = filtered_properties.filter(region=entered_region)

    if entered_project != '' and entered_project is not None:
      filtered_properties = filtered_properties.filter(project=entered_project)

    context = {
      "filtered_properties": filtered_properties,
    }
    return render(request, "haji_salam/filtered-properties.html", context)