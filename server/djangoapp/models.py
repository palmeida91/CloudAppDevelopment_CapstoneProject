from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    description = models.CharField(max_length=60)

    def __str__(self):
        return self.name + " " + self.description


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    #Many-to-One relationship to CarMake
    carMake = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    name = models.CharField(null=False,max_length=30)
    dealerId = models.IntegerField(default=0)

    SEDAN = "Sedan"
    SUV = "SUV"
    HATCHBACK = "Hatchback"
    COUPE = "Coupe"
    WAGON = "Wagon"
    CAR_CHOICE = [(SEDAN,"Sedan"),(SUV,"SUV"),(HATCHBACK,"Hatchback"),(COUPE,"Coupe"),(WAGON,"Wagon")]
    modelType = models.CharField(max_length=20, choices=CAR_CHOICE, default=SUV)
    modelYeal = models.DateField()

    def __str__(self):
        return self.carMake + " " + self.name + " " + self.modelType + " " + self.modelYeal


# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, state, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.state = state
        self.zip = zip

    def __str__(self):
        return self.full_name + ", " + self.state

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, id, name, purchase, review, carMake=None, carModel=None, carYear=None, purchaseDate=None, sentiment="neutral"):
        self.dealership = dealership
        self.id = id
        self.name = name
        self.purchase = purchase
        self.review = review
        self.carMake = carMake
        self.carModel = carModel
        self.carYear = carYear
        self.purchaseDate = purchaseDate
        self.sentiment = sentiment

    def __str__(self):
        return "Review by" + self.name + ": " + self.review
        

