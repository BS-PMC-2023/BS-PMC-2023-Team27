'''Models'''
from django.db import models

from django.contrib.auth.models import User
# Create your models here.


class Passenger(models.Model):
    '''Passenger'''
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True)
    id_user_P = models.IntegerField()


class Worker(models.Model):
    '''Worker'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    profile_pic = models.ImageField(
        upload_to='profile_pic/CustomerProfilePic/', null=True, blank=True)
    mobile = models.CharField(max_length=20, null=False)
    email = models.EmailField(null=False, default="")


class ContactUs(models.Model):
    '''ContactUs'''
    email = models.EmailField(null=False)
    subject = models.CharField(max_length=50, null=False)
    Discrbition = models.TextField()


class Workerreport(models.Model):
    '''workerreport'''
    email = models.EmailField(null=False)
    phonenumber = models.CharField(max_length=50, null=False)
    Discrbition = models.TextField()


class Report(models.Model):
    '''report'''
    email = models.EmailField(null=False)
    phonenumber = models.CharField(max_length=50, null=False)
    Discrbition = models.TextField()


class Flight(models.Model):
    '''Flight'''

    amount = models.IntegerField()
    arrivalDateTimeAway = models.DateTimeField()
    departureDateTimeA = models.DateTimeField()
    durationInMinutesA = models.IntegerField()
    away = models.CharField(max_length=1000)
    awayimg = models.ImageField()
    arrivalDateTimeR = models.DateTimeField()
    departureDateTimeR = models.DateTimeField()
    durationInMinutesR = models.IntegerField()
    returnf = models.CharField(max_length=1000)
    returnimg = models.ImageField()


class Order(models.Model):
    '''Order'''
    name = models.CharField(max_length=1000)
