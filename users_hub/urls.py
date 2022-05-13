from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'users_hub'

urlpatterns = [
    path('profile/', views.profile, name="profile"),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name="users_hub/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users_hub/logout.html"), name='logout'),
]