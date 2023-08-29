from django.shortcuts import render

from .models import Property

# Create your views here.

def home(request):
  latest_properties = Property.objects.all().order_by("-date")
  return render(request, "haji_salam/home.html", {
    'latest_properties': latest_properties,
  })