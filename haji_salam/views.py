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
      "purpose_choices": Property.PURPOSES,
      "type_choices": Property.TYPES,
      "city_choices": Property.CITIES,
      "regions_choices": Property.REGIONS,
      "project_choices": Property.PROJECTS,
    }
    return render(request, "haji_salam/prop-detail.html", context)
  

class filterProperty(View):
  def get(self, request):

    context = {
      "purpose_choices": Property.PURPOSES,
      "type_choices": Property.TYPES,
      "city_choices": Property.CITIES,
      "regions_choices": Property.REGIONS,
      "project_choices": Property.PROJECTS,
    }
    return render(request, "haji_salam/advanced-filtering.html", context)

  def post(self, request):
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


    if request.POST['get-path'] == "/advanced-search/":
      entered_min_area = request.POST['min-area']
      entered_max_area = request.POST['max-area']
      entered_min_price = request.POST['min-price']
      entered_max_price = request.POST['max-price']
      entered_reception_rooms = request.POST['reception-rooms']
      entered_bedrooms = request.POST['bedrooms']
      entered_bathrooms = request.POST['bathrooms']
      entered_kitchens = request.POST['kitchens']
      entered_garage = request.POST['garage']
      entered_balcony = request.POST['balcony']

      if entered_min_area != '' and entered_min_area is not None:
        filtered_properties = filtered_properties.filter(area__gte=entered_min_area)

      if entered_max_area != '' and entered_max_area is not None:
        filtered_properties = filtered_properties.filter(area__lte=entered_max_area)

      if entered_min_price != '' and entered_min_price is not None:
        filtered_properties = filtered_properties.filter(price__gte=entered_min_price)

      if entered_max_price != '' and entered_max_price is not None:
        filtered_properties = filtered_properties.filter(price__lte=entered_max_price)

      if entered_reception_rooms != '' and entered_reception_rooms is not None:
        filtered_properties = filtered_properties.filter(reception_rooms=entered_reception_rooms)

      if entered_bedrooms != '' and entered_bedrooms is not None:
        filtered_properties = filtered_properties.filter(bedrooms=entered_bedrooms)

      if entered_bathrooms != '' and entered_bathrooms is not None:
        filtered_properties = filtered_properties.filter(bathrooms=entered_bathrooms)

      if entered_kitchens != '' and entered_kitchens is not None:
        filtered_properties = filtered_properties.filter(kitchens=entered_kitchens)
        
      if entered_garage != '' and entered_garage is not None:
        filtered_properties = filtered_properties.filter(garage=entered_garage)
        
      if entered_balcony != '' and entered_balcony is not None:
        filtered_properties = filtered_properties.filter(balcony=entered_balcony)

    context = {
      "filtered_properties": filtered_properties,
    }
    return render(request, "haji_salam/filtered-properties.html", context)