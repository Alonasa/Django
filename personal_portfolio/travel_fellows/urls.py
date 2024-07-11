from django.urls import path
from . import views

urlpatterns = [
    path('', views.fellows, name="fellows"),
    path('destinations/', views.destinations, name="destinations"),
    path('companions/', views.companions, name="companions"),
    path('auth/', views.auth, name="authorize"),
    path('auth-form/', views.AuthorizeUser.as_view(), name="auth-user"),
    path('register-form/', views.RegisterUser.as_view(), name="register"),
    path('logout/', views.logOut, name="logout"),
    path('user/', views.ViewUserProfile.as_view(), name="user"),
]
