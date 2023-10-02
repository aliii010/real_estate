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


def applyFilter(entered_data, filtered_properties, **kwargs):
  if entered_data != '' and entered_data is not None:
      for key, value in kwargs.items():
        #key is the model field, and the value is the entered_data when calling the function
        return filtered_properties.filter(**{key: value})
  else: #if the entered_data is an empty string or is none then don't filter it.
    return filtered_properties


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
    entered_purpose = request.POST['purpose']
    entered_city = request.POST['city'].lower()
    entered_region = request.POST['region']
    entered_project = request.POST['project']
    entered_type = request.POST['type']
    
    filtered_properties = applyFilter(entered_purpose, filtered_properties, purpose=entered_purpose)
    filtered_properties = applyFilter(entered_city, filtered_properties, city=entered_city)
    filtered_properties = applyFilter(entered_region, filtered_properties, region=entered_region)
    filtered_properties = applyFilter(entered_project, filtered_properties, project=entered_project)
    filtered_properties = applyFilter(entered_type, filtered_properties, type=entered_type)

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

      filtered_properties = applyFilter(entered_min_area, filtered_properties, area__gte=entered_min_area)
      filtered_properties = applyFilter(entered_max_area, filtered_properties, area__lte=entered_max_area)
      filtered_properties = applyFilter(entered_min_price, filtered_properties, price__gte=entered_min_price)
      filtered_properties = applyFilter(entered_max_price, filtered_properties, price__lte=entered_max_price)
      filtered_properties = applyFilter(entered_reception_rooms, filtered_properties, reception_rooms=entered_reception_rooms)
      filtered_properties = applyFilter(entered_bedrooms, filtered_properties, bedrooms=entered_bedrooms)
      filtered_properties = applyFilter(entered_bathrooms, filtered_properties, bathrooms=entered_bathrooms)
      filtered_properties = applyFilter(entered_kitchens, filtered_properties, kitchens=entered_kitchens)
      filtered_properties = applyFilter(entered_garage, filtered_properties, garage=entered_garage)
      filtered_properties = applyFilter(entered_balcony, filtered_properties, balcony=entered_balcony)

    context = {
      "filtered_properties": filtered_properties,
    }
    return render(request, "haji_salam/filtered-properties.html", context)