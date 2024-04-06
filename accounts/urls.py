# In accounts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),  # Ensure it's 'register/' and not just 'register'
]

