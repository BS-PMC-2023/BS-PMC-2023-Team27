"""FlyBetter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path

from Boards import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout', LogoutView.as_view(next_page='home'), name='logout'),
    path('HomePageadmin', views.HomePageadmin, name='HomePageadmin'),
    path('homePageWorker', views.homePageWorker, name='homePageWorker'),
    path('homePage', views.Home, name='homePage'),
    path('SignUp',views.SignUp,name='SignUp'),
    path('SignUpPage', views.SignUpPage, name='SignUpPage'),
    path('',views.LogIN,name='home'),
    path('worker_signup', views.worker_signup, name='worker_signup'),
    path('About',views.about,name='About'),
    
]
