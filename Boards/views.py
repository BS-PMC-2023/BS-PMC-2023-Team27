from django.shortcuts import render,HttpResponse,redirect
from .models import USER
from django.contrib import messages
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