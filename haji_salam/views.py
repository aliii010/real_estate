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

  def apply_filter(self, entered_data, filtered_properties, **kwargs):
    if entered_data != '' and entered_data is not None:
      for key, value in kwargs.items():
        #key is the model field, and the value is the entered_data when calling the function
        return filtered_properties.filter(**{key: value})
    else: #if the entered_data is an empty string or is none then don't filter it.
      return filtered_properties
    
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
    field_data = {
      "purpose": request.POST['purpose'],
      "city": request.POST['city'],
      "region": request.POST['region'],
      "project": request.POST['project'],
      "type": request.POST['type'],
    }

    if request.POST['get-path'] == "/advanced-search/":
      field_data = {
        "purpose": request.POST['purpose'],
        "city": request.POST['city'],
        "region": request.POST['region'],
        "project": request.POST['project'],
        "area__gte": request.POST['min-area'],
        "area__lte": request.POST['max-area'],
        "price__gte": request.POST['min-price'],
        "price__lte": request.POST['max-price'],
        "reception_rooms": request.POST['reception-rooms'],
        "bedrooms": request.POST['bedrooms'],
        "bathrooms": request.POST['bathrooms'],
        "kitchens": request.POST['kitchens'],
        "garage": request.POST['garage'],
        "balcony": request.POST['balcony'],
      }

    for model_field, entered_data in field_data.items():
      kwargs = {
        model_field: entered_data,
      }
      filtered_properties = self.apply_filter(entered_data, filtered_properties, **kwargs)

    context = {
      "filtered_properties": filtered_properties,
    }
    return render(request, "haji_salam/filtered-properties.html", context)