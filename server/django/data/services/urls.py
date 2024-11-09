
from django.urls import path
from .views import *


urlpatterns = [
    path("drawer/<int:id>", drawer, name="drawer"),
    path("sort/<path:arr>", sort, name='sort'),
    path("shell", shell, name='shell')
]