from django.contrib import admin
from .models import User, UserProfile, HashTag, UserTransportation, UserPlans

# Register your models here.

admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(HashTag)
admin.site.register(UserTransportation)
admin.site.register(UserPlans)
