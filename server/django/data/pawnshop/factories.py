from factory import Faker
from factory.django import DjangoModelFactory
from .models import City

locale = "ru_RU"
  
    
class CityFactory(DjangoModelFactory):
    class Meta:
        model = City
        
        
    name = Faker('city_name', locale=locale)
    country = Faker('country', locale=locale)
    mayor = Faker('name', locale=locale)
    postcode = Faker('postcode', locale=locale)
    number = Faker('random_int', min=1e4, max=1e6, locale=locale)
    
    
def populate_cities():
    cities = CityFactory.create_batch(50)
    return cities