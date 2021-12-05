from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def login_user(request):
    ctx = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ('Niepoprawne dane logowania'))
            return redirect('login')
    else:
        return render(request, 'authenticate/login.html', ctx)

def logout_user(request):
    logout(request)
    messages.success(request, ('Zostałeś wylogowany poprawnie'))
    return redirect('home')
