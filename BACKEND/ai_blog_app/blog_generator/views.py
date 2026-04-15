from django.shortcuts import render

# Create your views here.
def index(request):  #creating index function that takes in request
    return render(request, 'index.html')