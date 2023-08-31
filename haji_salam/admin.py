from django.contrib import admin
from .models import Property, PropertyImage, City

# Register your models here.

class PropertyImageInline(admin.StackedInline):
  model = PropertyImage

class PropertyAdmin(admin.ModelAdmin):
  inlines = [
    PropertyImageInline,
  ]

  prepopulated_fields = {
    "prop_slug": ("title",),
  }


admin.site.register(Property, PropertyAdmin)
admin.site.register(PropertyImage)
admin.site.register(City)