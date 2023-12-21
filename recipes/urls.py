from django.urls import path
from pip._vendor.requests.api import request

from recipes.views import home

urlpatterns = [
    path('', home),  # HOME
]
