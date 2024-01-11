from django.urls import path
from home.views import Home
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('',Home.as_view(), name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='home/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='home/login.html'),name='logout'),
]