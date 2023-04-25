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
        fields = ['mobile', 'profile_pic','id_user']