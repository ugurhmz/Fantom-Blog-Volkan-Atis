
from django.urls import path
from .views import *
from django.contrib.auth import views as authViews
from django.urls import reverse_lazy


app_name="users"
urlpatterns = [

    path('register/', RegisterView.as_view(), name='register'),
    path('login/',UserLogin.as_view(), name='login'),
    path('logout/',UserLogout.as_view(), name='logout'),
    path('password-change/', authViews.PasswordChangeView.as_view(success_url=reverse_lazy('users:password_change_done')), name='password_change'),
    path('password-change-done/', authViews.PasswordChangeDoneView.as_view(), name='password_change_done'),


]