from django.contrib.auth import logout
from django.shortcuts import render,HttpResponse,redirect

from . import forms
from .models import USER
from django.contrib import messages
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
# Create your views here.

def Home(request):
  
    return render(request,'index.html')

def SignUp(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request,'Password do not match')
            return redirect('SignUp')
        try:
            user =  USER.objects.create(username=username,email=email,password=password1)
            user.save()
            messages.success(request,'User created successfully!')
            return redirect('LogIn')
        except:
            messages.error(request,'Error crating user!')

    return render(request,'SignUp.html')

def LogIN(request):
    if request == 'POST':
        print("kjhdfjs")
        username = request.POST['username']
        password1 = request.POST['pass']
        user = USER.objects.get(username)
        print(password1)
        print(user.password)
        if user.password == password1:
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')

    print("aaaaaaaa")
    return render(request,'LogIn.html')


def worker_signup(request):
    userForm = forms.WorkerUserForm()
    workerForm = forms.WorkerForm()

    mydict = {'userForm': userForm, 'workerForm': workerForm}
    if request.method == 'POST':
        userForm = forms.WorkerUserForm(request.POST)
        workerForm = forms.WorkerForm(request.POST, request.FILES)
        print(workerForm.is_valid())
        if userForm.is_valid() and workerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            worker = workerForm.save(commit=False)
            worker.user = user
            worker.save()
            my_customer_group = Group.objects.get_or_create(name='WORKER')
            my_customer_group[0].user_set.add(user)
        return HttpResponseRedirect('LogIn')
    return render(request, 'workersignup.html', context=mydict)


def logOut(request):
    logout(request)