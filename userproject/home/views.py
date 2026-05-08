from django.shortcuts import render,redirect
from django.contrib.auth.models import user
from django.contrib.auth import authenticate,logout

# pw for aashi is Aashika123
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return render(request, "login.html")

    else:
        return render(request,"index.html")

def login(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(username=username,password=password)
        if user is not None:
            return redirect('/')
        else:
            return render(request,"login.html")

def logout(request):
    return render(request,"login.html")