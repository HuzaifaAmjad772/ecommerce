from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login , logout
from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password_confirm']

        if password != confirm_password:
            messages.error(request, "Passwords don't match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        user.save()
        auth_login(request, user)
        return redirect('home')

    return render(request, 'register.html')


def login_view(request): 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            auth_login(request, user)  
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials!")
            return redirect('login')

    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('home')