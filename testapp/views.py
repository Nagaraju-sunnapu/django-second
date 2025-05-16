from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime
def display(request):
    time=datetime.datetime.now()
    s='<h1> now the server time is: ' +str(time) + ' </h1>'
    return HttpResponse(s)