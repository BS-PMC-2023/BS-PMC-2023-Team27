from django import forms
from django.contrib.auth.models import User

from . import models


class WorkerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class WorkerForm(forms.ModelForm):
    class Meta:
        model = models.Worker
        fields = ['mobile', 'profile_pic', 'id_user','email']


class PassengerUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()

        }


class PassengerForm(forms.ModelForm):
    class Meta:
        model = models.Passenger
        fields = ['id_user_P']

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = models.ContactUs
        fields = ['email', 'subject', 'Discrbition']

class workerreportForm(forms.ModelForm):
    class Meta:
        model = models.workerreport
        fields = ['email', 'phonenumber', 'Discrbition']
