from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignUpForm

from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm



# Create your views here.
def home_view(request,*args, **kwargs):
    #This function loads the template with the given name and returns a Template object
    #template = loader.get_template('Home/home.html')
    return render(request,'Home/home.html',{})

def start_page_view(request,*args, **kwargs):
    return render(request,'StartPage/start_page.html',{})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('profile')
    else:
        form = SignUpForm()
    return render(request, 'signUp/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(user.email)
            login(request, user)
            return redirect('profile')
            #return redirect('profile2', user=user)
    else:
        form = AuthenticationForm()
    return render(request, 'Login/login_page.html', {'form': form})

def profile_view(request):
    kwargs = {'user':request.user}
    return render(request, 'Profile/profile.html', kwargs)

def data_view(request):
    if request.method == 'POST':
        user_form=UserChangeForm(request.POST, instance = request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('profile')

    else:
        user_form=UserChangeForm(instance = request.user)
        context={
            'form':user_form
        }
        return render(request, 'Data/data.html', context)

def marshrutes_view(request):
    return render(request, 'Marshrutes/marshrutes.html', {})

def founders_view(request):
    return render(request, 'Founders/founders.html', {})

def contacts_view(request):
    return render(request, 'Contacts/contacts.html', {})


def about_view(request):
    return render(request, 'About/about.html', {})




#it works but it's not needed, it makes page for every profile in the database
#def profile_dynamic_view(request, user):
#    return render(request, 'Profile/profile.html', {'user':user})