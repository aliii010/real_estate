from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home-page"),
  path("all-properties", views.allProperties.as_view(), name="all-properties-page")
]
