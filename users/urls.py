
from django.urls import path, include

from . import views

app_name = 'users'
urlpatterns = [
    # Include default auth urls.
    path('', include('django.contrib.auth.urls')),
    # Registration page.
    path('sign_up/', views.sign_up, name='sign_up'),
    # Log out page.
    path('log_out/', views.logged_out, name='logged_out'),
    # Log in page
    path('login_user/', views.login_user, name='login_user'),
    # Admin's sign up page.
    path('admin_sign_up', views.admin_sign_up, name='admin_sign_up'),
    # Admin log in page
    path('login_admin/', views.login_admin, name='login_admin')
]