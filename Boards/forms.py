'''FormsFile'''
from django import forms
from django.contrib.auth.models import User

from models import Passenger, Worker, ContactUs, Workerreport


class WorkerUserForm(forms.ModelForm):
    '''WorkerUserform'''
    class Meta:
        '''ModleUser'''

        def pub1(self):
            """pub1 """

        def pub2(self):
            """pub2 """

        model = User
        fields = ['first_name', 'last_name', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput()
        }


class WorkerForm(forms.ModelForm):
    '''WorkerForm'''
    class Meta:
        '''modleWorker'''

        def pub1(self):
            """pub1 """

        def pub2(self):
            """pub2 """

        model = Worker
        fields = ['mobile', 'profile_pic', 'id_user', 'email']


class PassengerUserForm(forms.ModelForm):
    '''PassengerUserForm'''
    class Meta:
        '''ModlePassngermodle'''

        def pub1(self):
            """pub1 """

        def pub2(self):
            """pub2 """
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput()

        }


class PassengerForm(forms.ModelForm):
    "PassengerForm"
    class Meta:
        "modlePassnger"

        def pub1(self):
            """pub1 """

        def pub2(self):
            """pub2 """

        model = Passenger
        fields = ['id_user_P']


class ContactUsForm(forms.ModelForm):
    '''ContactUsForm'''
    class Meta:
        '''modleContactUs'''

        def pub1(self):
            """pub1 """

        def pub2(self):
            """pub2 """

        model = ContactUs
        fields = ['email', 'subject', 'Discrbition']


class WorkerReportForm(forms.ModelForm):
    '''workerreportForm'''
    class Meta:
        '''modleworkerreport'''

        def pub1(self):
            """pub1 """

        def pub2(self):
            """pub2 """

        model = Workerreport
        fields = ['email', 'phonenumber', 'Discrbition']
