# from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index,name='home'),
    path('about',views.about,name='about'),
    path('services',views.services,name='services'),
    path('contacts',views.contacts,name='contacts'),
    path('/services/web',view.web,name='web'),
    path('/services/app',view.app,name='app'),
    path('/services/design',view.design,name='design'),
]