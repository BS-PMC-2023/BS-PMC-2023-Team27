from django.contrib.auth import logout
from django.shortcuts import render,redirect



from django.contrib import messages, auth
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

# Create your views here.

def Home(request):
    return render(request,'index.html')

def about(request):

    return render(request,'aboutus.html')

def SignUp(request):
    passngeruserform = forms.PassengerUserForm()
    PassengerForm=forms.PassengerForm()
    mydict = {'PassengerForm': PassengerForm,'passngeruserform':passngeruserform}

    if request.method == 'POST':
        userPForm = forms.PassengerUserForm(request.POST)
        PassngerForm = forms.PassengerForm(request.POST, request.FILES)
        if userPForm.is_valid() and PassngerForm.is_valid() :
            print("bbbb")
            user = userPForm.save()
            user.set_password(user.password)
            user.save()
            passenger = PassngerForm.save(commit=False)
            passenger.user = user
            passenger.save()
            my_customer_group = Group.objects.get_or_create(name='PASSENGER')
            my_customer_group[0].user_set.add(user)
            return redirect('home')
        else:
            print("aaa")
            messages.error(request, 'Password do not match')
            return redirect('SignUp')
        

    return render(request, 'SignUp.html', context=mydict)

'''def LogIN(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_staff:
                auth.login(request, user)
                return redirect('Home')
        return redirect('Home')
    else:
        messages.error(request, 'Invalid username or password')
        return render(request, 'LogIn.html')'''

def LogIN(request):
    print(request.user.is_authenticated)
    if request.user.is_authenticated == False:
        if request.method == "POST":

            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_staff:
                auth.login(request, user)
                return redirect('HomePageadmin')
            elif user is not None and user.groups.filter(name='PASSENGER').exists():
                auth.login(request, user)
                return redirect('homePage')
            elif user is not None and user.groups.filter(name='WORKER').exists():
                auth.login(request, user)
                return redirect('homePageWorker')
    else:
        if request.user.is_staff:
            return redirect('HomePageadmin')
        elif request.user.groups.filter(name='WORKER'):
            return redirect('homePageWorker')
        elif request.user.groups.filter(name='PASSENGER'):
            return redirect('homePage')
    return render(request,'LogIn.html')




def worker_signup(request):
    userForm = forms.WorkerUserForm()
    workerForm = forms.WorkerForm()
    mydict = {'userForm': userForm, 'workerForm': workerForm}
    if request.method == 'POST':
        userForm = forms.WorkerUserForm(request.POST)
        workerForm = forms.WorkerForm(request.POST, request.FILES)
        if userForm.is_valid() and workerForm.is_valid():
            user = userForm.save()
            user.set_password(user.password)
            user.save()
            worker = workerForm.save(commit=False)
            worker.user = user
            worker.save()
            my_customer_group = Group.objects.get_or_create(name='WORKER')
            my_customer_group[0].user_set.add(user)
        return redirect('HomePageadmin')
    return render(request, 'workersignup.html', context=mydict)


def logOut(request):
    logout(request)

def HomePageadmin(request):
    return render(request,'HomePageadmin.html')

def homePageWorker(request):
    return render(request,'homePageWorker.html')

def SignUpPage(request):
    return render(request,'SignUp.html')
