from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome(request):
    print("step-1")
    return render(request, "website/mainpage.html")