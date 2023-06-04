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
    path('homePage', views.homePage, name='homePage'),
    path('home', views.homePage, name='home'),
    path('SignUp', views.SignUp, name='SignUp'),
    path('SignUpPage', views.SignUpPage, name='SignUpPage'),
    path('', views.LogIN, name='home'),
    path('worker_signup', views.worker_signup, name='worker_signup'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('paypal', views.paypal, name='paypal'),
    path('ContactUs', views.ContactUs, name='ContactUs'),
    path('Contact', views.Contact, name='Contact'),
    path('workerreport', views.workersReport, name='workerreport'),
    path('viewAllReports', views.viewAllReports, name='viewAllReports'),
    path('EditWorker', views.EditWorker, name='EditWorker'),
    path('EditWorkerusername/<int:id>',views.EditWorkerusername, name='EditWorkerusername'),
    path('EditWorkerIDuser/<int:id>',views.EditWorkerIDuser, name='EditWorkerIDuser'),
    path('EditWorkerEmail/<int:id>', views.EditWorkerEmail, name='EditWorkerEmail'),
    path('EditWorkermobile/<int:id>', views.EditWorkermobile, name='EditWorkermobile'),
    path('vieworders', views.vieworders, name='vieworders'),
    path('airline', views.airline, name='airline'),
    path('SearchFilght', views.SearchFilght, name='SearchFilght'),
    path('menu', views.menu, name='menu'),
    path('getorder', views.getorder, name='getorder'),
    path('Filght', views.Filght, name='Filght'),













]
