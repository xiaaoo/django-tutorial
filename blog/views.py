from django.shortcuts import render
from django.http import HttpResponse

# this is the logic for how we want to handle when the user goes to blog home page
def home(request):
    return HttpResponse('<h1>Blog Home</h1>')

def about(request):
    return HttpResponse('<h1>Blog About</h1>')