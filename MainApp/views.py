from django.shortcuts import render, HttpResponse

def home(request):
    return HttpResponse('<h1><b>Welcome to our site!</b></h1>')
