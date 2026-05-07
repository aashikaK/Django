from django.shortcuts import render,redirect



# pw for aashi is Aashika123
# Create your views here.
def index(request):
    return render(request,"index.html")
def login(request):
    return render(request,"login.html")
def logout(request):
    return render(request,"login.html")