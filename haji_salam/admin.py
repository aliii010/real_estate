from django.contrib import admin
from .models import Property, PropertyImage, City

# Register your models here.

class PropertyImageInline(admin.StackedInline):
  model = PropertyImage

class PropertyAdmin(admin.ModelAdmin):
  inlines = [
    PropertyImageInline,
  ]


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage)
admin.site.register(City)