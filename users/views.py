from django.contrib.auth import authenticate, login
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


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:

                return HttpResponse("error")
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
