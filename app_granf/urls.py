from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dash/', views.dash, name='dash'),  
    path('logout/', views.home, name='logout'),  
]
