from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def list_client(request):
    return render(request,'CLIENT/list_client.html')