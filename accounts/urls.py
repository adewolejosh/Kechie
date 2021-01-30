from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    # signup
    path('signup/', views.SignUpView.as_view(), name='signup'),
    # login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    # logout
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # profile
    path('profile/', views.profile, name='profile'),
]
