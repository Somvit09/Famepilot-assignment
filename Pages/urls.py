from django.urls import path
from . import views
from .views import login_view, logout_view, registration_view, account_view
from knox import views as knox_views
urlpatterns = [
    path('register', registration_view, name='register'),
    path('login', login_view, name='login'),
    path('logout', logout_view, name='logout'),
    path('dashboard', account_view, name='dashboard')
]
