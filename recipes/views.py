from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def sobre(request):
    return HttpResponse('sobre')
    # RETURN HTTP RESPONSE
def contato(request):
    return HttpResponse('contato')
    # RETURN HTTP RESPONSE