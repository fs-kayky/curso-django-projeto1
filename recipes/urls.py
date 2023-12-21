from django.urls import path
from pip._vendor.requests.api import request

from recipes.views import contato, home, sobre

urlpatterns = [
    path('', home),  # HOME
    path('sobre/', sobre),  #SOBRE
    path('contato/', contato),  #CONTATO
]
