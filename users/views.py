from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UniversityForm, LoginForm
from django.contrib import messages
from django.http import HttpResponse


# Create your views here.
def signup(request):
    form = UniversityForm(request.POST or None)
    if form.is_valid():
        user = form.save()
        user.set_password(form.cleaned_data['password'])
        user.save()
        messages.success(request, "Registered Successfully")
    context = {'form': UniversityForm()}
    return render(request, 'users/index.html', context)


def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    else:
        return render(request, 'users/login.html')
    return render(request, 'users/login.html')


def home(request):
    return render(request, 'users/home.html')


def Logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect('login')
