from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login, logout
from account.models import MyUser
from django.core.cache import cache


def signin(request):
    if request.method == "POST":
        try:
            email, password = request.POST.get(
                'email'), request.POST.get('password')
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                if request.user.user_type == 2:
                    messages.success(request, 'Welcome Admin !')
                    return redirect(reverse_lazy('admin_home'))
                messages.success(request, 'Welcome Student')
                return redirect(reverse_lazy('student_home'))
            messages.error(request, 'Invalid Credentials')
        except:
            messages.error(request, 'Some Error Occured!')
            return redirect(reverse_lazy('signin'))
    return render(request, 'login.html')


def signout(request):

    try:
        logout(request)
        cache.clear()
        return redirect(reverse_lazy('signin'))
    except:
        return redirect(reverse_lazy('signin'))


def index(request):
    return render(request, 'index.html')


def register(request):
    try:
        if request.method == "POST":
            print('e')
            fname = request.POST.get('fname')
            email = request.POST.get('email')
            number = request.POST.get('number')
            pass1 = request.POST.get('pass1')
            pass2 = request.POST.get('pass2')
            if pass1 != pass2:
                messages.error(request, 'Password Not Match!')
                return redirect(reverse_lazy('signin'))
            print('g')
            print(MyUser.objects.all().filter(email=email).exists())
            if MyUser.objects.all().filter(email=email).exists():
                messages.error(request, "Email Already Taken!")
                return redirect(reverse_lazy('register'))
            print('s')
            new_user = MyUser.objects.create_user(email=email, password=pass1, phone=number, first_name=fname)
            new_user.save()
            if request.FILES:
                print('e')
                new_user.picture = request.FILES['img']
                new_user.save()
            messages.success(
                request, 'Acount Created Successfully. Please Login')
            return redirect(reverse_lazy('signin'))
    except:
        messages(request,'')
        return render(request, 'registration.html')
    return render(request, 'registration.html')
