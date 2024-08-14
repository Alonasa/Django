from cities_light.loading import get_cities_models
from django.contrib import admin
from .models import User, UserProfile, HashTag, UserTransportation, UserPlans

# Register your models here.
Country, Region, SubRegion, City = get_cities_models()

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(HashTag)
admin.site.register(UserTransportation)
admin.site.register(UserPlans)
