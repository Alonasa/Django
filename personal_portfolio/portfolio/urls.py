from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('fellows/', views.fellows, name="project-fellows"),
    path('generator/', include('pass_generator.password_generator.urls')),
]

