from django.contrib import admin
from .models import CarMake,CarModel


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 2

# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    listDisplay = ['carMake', 'name', 'dealerId', 'modelType', 'modelYear']
    listFilter = ['modelType', 'carMake', 'dealerId', 'modelYear',]
    searchFields = ['carMake', 'name']

# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    listDisplay = ['name', 'description']
    searchFields = ['name']
    inlines = [CarModelInline]

# Register models here
admin.site.register(CarMake,CarMakeAdmin)
admin.site.register(CarModel,CarModelAdmin)