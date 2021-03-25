
from django.urls import path
from .views import *


app_name="users"
urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/',UserLogin.as_view(), name='login'),
    path('logout/',UserLogout.as_view(), name='logout'),


]