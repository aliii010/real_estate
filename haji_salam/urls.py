from django.urls import path
from . import views

urlpatterns = [
  path("", views.home, name="home-page"),
  path("properties", views.allProperties.as_view(), name="all-properties-page"),
  path("properties/<slug:slug>/", views.PropertyDetail.as_view(), name="detail-page"),
  path("advanced-search/", views.filterProperty.as_view(), name="advanced-search"), #for get requests (when the advanced search page is loaded)
  path("filtered-properties/", views.filterProperty.as_view(), name="filtered-properties"), #for post requests (when the filtering form is submitted)
]
