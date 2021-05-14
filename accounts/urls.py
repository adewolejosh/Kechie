from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .decorators import unauthenticated_user


urlpatterns = [
    # signup
    path('signup/', unauthenticated_user(views.SignUpView.as_view()), name='signup'),
    # login
    # @login_pass_test
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True, template_name='login.html'), name='login'),
    # logout
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    # profile
    path('profile/', views.profile, name='profile'),
]
