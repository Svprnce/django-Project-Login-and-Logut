from django.conf import settings
from django.urls import path
from authentication import views



urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
] 