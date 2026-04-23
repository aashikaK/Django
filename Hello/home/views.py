from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("This is homepage.")
    context={'name':"Aashika",'age':22,'salary':4500000}
    return render(request,'index.html',context)

def about(request):
    return HttpResponse("This is about page")

def services(request):
    return HttpResponse('This is services page')

def contacts(request):
    return HttpResponse('This is contacts page')