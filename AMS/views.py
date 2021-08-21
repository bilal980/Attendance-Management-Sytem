from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
def signin(request):
    if request.method=="POST":
        try:
            email, password = request.POST.get('email'),request.POST.get('password')
            user=authenticate(request,email=email,password=password)
            if user is not None:
                login(request,user)
                if request.user.is_admin:
                    messages.success(request,'Welcome Admin !')
                    return redirect(reverse_lazy('admin_home'))
                messages.success(request,'Welcome Student')
                return redirect(reverse_lazy('student_home'))
            messages.error(request,'Invalid Credentials')
        except:
            messages.error(request,'Some Error Occured!')
            return redirect(reverse_lazy('signin'))
    return render(request,'login.html')

def signout(request):
    try:
        logout(request)
        return redirect(reverse_lazy('signin'))
    except:
        return redirect(reverse_lazy('signin'))

def index(request):
    return render(request,'index.html')


def register(request):
    return render(request,'registration.html')
