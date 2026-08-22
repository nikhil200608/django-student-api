from django.urls import path
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

from . import views


urlpatterns = [
    path(
        'register/',
        views.register_view,
        name='register',
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='accounts/login.html'
        ),
        name='login',
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout',
    ),

    path(
        'api/login/',
        obtain_auth_token,
        name='api_token_login',
    ),

    path(
        'api/logout/',
        views.api_logout,
        name='api_token_logout',
    ),
]