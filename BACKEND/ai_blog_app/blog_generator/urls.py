from django.urls import path
from . import views

urlpatterns = [  #Is going to take a list of all urls that we have in our application
    path('', views.index, name='index')  # Creating a url that is specified for the homepage. Whenever a user is trying to go to the homepage, he's going to go to the views file and look for the function named index, and whatever is being done in that function is what is going to be rendered for this url
]