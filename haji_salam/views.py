from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from .models import Property

# Create your views here.

def home(request):
  latest_properties = Property.objects.all().order_by("-date")
  return render(request, "haji_salam/home.html", {
    'latest_properties': latest_properties,
  })

class allProperties(ListView):
  template_name = 'haji_salam/all-properties.html'
  model = Property
  ordering = ["-date"]
  context_object_name = "all_properties"


class PropertyDetail(View):
  def get(self, request, slug):
    identified_prop = Property.objects.get(prop_slug=slug)
    print(identified_prop)