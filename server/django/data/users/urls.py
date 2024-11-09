from django.urls import path
from .views import *


urlpatterns = [
    path('register/', sign_up, name='register'),
    path('login/', sign_in, name='login'),
    path('logout/', sign_down, name='logout'),
    path('settings/', settings, name="settings")
]