from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is homepage.")
    context={'name':"Aashika",'age':22,'salary':4500000} #dict but it sends...
    return render(request,'index.html',context)   #....individual keys in html like name age and salary from render

def about(request):
    return render(request,'about.html')
    # return HttpResponse("This is about page")

def services(request):
     return render(request,'services.html')
    # return HttpResponse('This is services page')

def contacts(request):
    return render(request,'contact.html')
    # return HttpResponse('This is contacts page')
def web(request):
    # return HttpResponse('This is web page of services')
    return render(request,'services-web.html')
def app(request):
    return HttpResponse('This is app page of services')
def design(request):
    return HttpResponse('This is design page of services')