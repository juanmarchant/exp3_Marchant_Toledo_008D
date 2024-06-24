from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login

from .forms import RegisterUserForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def register(request):
    data = {
        'form': RegisterUserForm()
    }
    if request.method == 'POST':
        formy = RegisterUserForm(data=request.POST)
        if formy.is_valid():
            formy.save()
            user = authenticate(username= formy.cleaned_data['username'] ,
            password = formy.cleaned_data['password1'] )
            login(request, user)
            return redirect('index')
        data['form'] = formy
    return render(request, 'registration/register.html', data)


@login_required
def shop(request):
    return render(request, 'shop.html')

def logout_view(request):
    logout(request)
    return redirect('/')