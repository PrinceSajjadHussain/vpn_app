from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Add this line
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
]
