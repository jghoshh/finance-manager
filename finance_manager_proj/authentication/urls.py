from django.urls import path
from . import views

app_name = 'authentication'

urlpatterns = [
    path('register', views.RegistrationView.as_view(), name='register'),
    path('login', views.LoginView.as_view(), name='login'),
    path('username_validation', views.username_validation, name='validate-username'),
    path('email_validation', views.email_validation, name='validate-email'), 
    path('logout', views.LogoutView.as_view(), name='logout')
]
 