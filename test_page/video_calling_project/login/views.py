from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your views here.

# Custom Form from the django default form
class RegistrationForm(UserCreationForm) :
    class Meta :
        model = User 
        fields = ["username", "email", "password", "password2"]



def signup(request) :
    form = RegistrationForm()

    if request == 'POST' :

        # getting the users details
        details = RegistrationForm(request.POST)
        
        # validating using django method 

        if details.is_valid() :
            # saving the details
            details.save()

    context = {'form' : form}
    return render(request, 'login/signup.html', context)


def login(request) :
    return render(request, 'login/login.html')
