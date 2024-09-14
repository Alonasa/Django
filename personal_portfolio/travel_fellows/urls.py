from django.urls import path
from . import views

urlpatterns = [
    path('', views.fellows, name="fellows"),
    path('destinations/', views.destinations, name="destinations"),
    path('companions/', views.companions, name="companions"),
    path('auth/', views.auth, name="authorize"),
    path('auth-form/', views.AuthorizeUser.as_view(), name="auth-user"),
    path('register-form/', views.RegisterUser.as_view(), name="register"),
    path('logout/', views.log_out, name="logout"),
    path('user/', views.UserProfileView.as_view(), name="user"),
    path('user-plans', views.handle_plans, name="user-plans"),
    path('user-plans/update/<int:plan_id>/', views.UserProfileView.as_view(), name='update_plan'),
    path('countries-data/', views.get_country_codes, name='countries-data')
]

