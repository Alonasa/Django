from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('fellows/', include('travel_fellows.urls'), name="project-fellows"),
    path('generator/', include('pass_generator.password_generator.urls')),
]

