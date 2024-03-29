
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.shortcuts import render, redirect
import urllib
import random
from datetime import datetime
import json

import requests
import pip._vendor.requests

from Boards import forms

from Boards.models import Flight, Order


from django.contrib import messages, auth
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from . import models
from .models import Passenger
from .models import Worker
from django.shortcuts import get_object_or_404





def homePage(request):
    """
    This function returns the rendered template 'index.html'.
    """
    return render(request, 'index.html')


def aboutus(request):
    """
    This function returns the rendered template 'aboutus.html'.
    """

    return render(request, 'aboutus.html')


def SignUp(request):
    """
    This function handles the sign-up process for passengers. It saves the user and passenger details
    to the database and redirects to the 'homePage' view. It also performs form validation.
    """
    passngeruserform = forms.PassengerUserForm()
    PassengerForm = forms.PassengerForm()
    mydict = {'PassengerForm': PassengerForm,
              'passngeruserform': passngeruserform}

    if request.method == 'POST':
        userPForm = forms.PassengerUserForm(request.POST)
        PassngerForm = forms.PassengerForm(request.POST, request.FILES)
        if userPForm.is_valid() and PassngerForm.is_valid():
            user = userPForm.save()
            user.set_password(user.password)
            user.save()
            passenger = PassngerForm.save(commit=False)
            passenger.user = user
            passenger.save()
            my_customer_group = Group.objects.get_or_create(name='PASSENGER')
            a = Group
            my_customer_group[0].user_set.add(user)
            return redirect('homePage')
        else:
            messages.error(request, 'Password do not match')
            print('error pass')
            return redirect('SignUp')

    return render(request, 'SignUp.html', context=mydict)



def LogIN(request):
    """
    This function handles the login process for users. It authenticates the user and redirects to the
    appropriate homepage based on the user's role (admin, worker, passenger). It also checks if the user
    is already authenticated and redirects accordingly.
    """
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
    return render(request, 'LogIn.html')


def worker_signup(request):
    """
    This function handles the sign-up process for workers. It saves the user and worker details
    to the database and redirects to the 'HomePageadmin' view. It also performs form validation.
    """
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
    """
    This function returns the rendered template 'logout.html'.
    """
    logOut(request)


def HomePageadmin(request):
    """
    This function returns the rendered template 'HomePageadmin.html'.
    """
    return render(request, 'HomePageadmin.html')


def homePageWorker(request):
    """
    This function returns the rendered template 'homePageWorker.html'.
    """
    return render(request, 'homePageWorker.html')


def SignUpPage(request):
    """
    This function returns the rendered template 'SignUp.html'.
    """
    return render(request, 'SignUp.html')


def paypal(request):
    """
    This function returns the rendered template 'paypal.html'.
    """
    return render(request, "paypal.html")


def ContactUs(request):
    """
    This function handles the contact form submission. It saves the contact details to the database and
    redirects to the 'homePage' view. It also performs form validation.
    """
    if request.method == 'POST':
        CousForm = forms.ContactUsForm(request.POST)
        print(CousForm)
        print(CousForm.is_valid())

        if CousForm.is_valid():
            contact = CousForm.save(commit=False)
            contact.save()
            my_customer_group = Group.objects.get_or_create(name='ContactUs')

        return redirect('homePage')
    else:
        return render(request, 'ContactUs.html')


def Contact(request):
    """
    This function returns the rendered template 'ContactUs.html'.
    """
    return render(request, 'ContactUs.html')


def workersReport(request):
    """
    This function handles the worker report submission. It saves the report details to the database and
    redirects to the 'homePageWorker' view. It also performs form validation.
    """

    if request.method == 'POST':

        wo_re = forms.workerreportForm(request.POST)
        print(wo_re.is_valid())

        if wo_re.is_valid():
            report = wo_re.save(commit=False)
            report.save()
            my_customer_group = Group.objects.get_or_create(
                name='workerreport')

        return redirect('homePageWorker')
    else:
        return render(request, 'workerreport.html')




def viewAllReports(request):
    """
    This function retrieves all worker reports from the database and renders them in the 'viewAllReports.html' template.
    """
    context = {}
    if request.method == 'GET':
        result = models.workerreport.objects.all()
        context = {"result": result}
    return render(request, 'viewAllReports.html', context=context)


def EditWorker(request):
    """
    This function retrieves all workers from the database and renders them in the 'EditWorker.html' template.
    """

    context = {}
    if request.method == 'GET':
        result = models.Worker.objects.all()
        context = {"result": result}
    return render(request, 'EditWorker.html', context=context)


def EditWorkerusername(request, id):
    """
    This function handles the edit of a worker's username. It updates the worker's username in the database and
    redirects to the 'EditWorker' view.
    """

    print("id", id)
    if request.method == 'POST':
        worker = models.Worker.objects.get(user_id=id)
        worker.user.username = request.POST['username']
        worker.user.save()
        return redirect('EditWorker')
    return render(request, 'EditWorkerusername.html')


def EditWorkerIDuser(request, id):
    """
    This function handles the edit of a worker's ID user. It updates the worker's ID user in the database and
    redirects to the 'EditWorker' view.
    """

    if request.method == 'POST':
        worker = models.Worker.objects.get(user_id=id)
        worker.id_user = request.POST['id_user']
        worker.save()
        return redirect('EditWorker')
    return render(request, 'EditWorkerIDuser.html')


def EditWorkerEmail(request, id):
    """
    This function handles the edit of a worker's email. It updates the worker's email in the database and
    redirects to the 'EditWorker' view.
    """

    if request.method == 'POST':
        worker = models.Worker.objects.get(user_id=id)
        worker.email = request.POST['email']
        worker.save()
        return redirect('EditWorker')
    return render(request, 'EditWorkerEmail.html')


def EditWorkermobile(request, id):
    """
    This function handles the edit of a worker's mobile. It updates the worker's mobile in the database and
    redirects to the 'EditWorker' view.
    """

    if request.method == 'POST':
        worker = models.Worker.objects.get(user_id=id)
        worker.mobile = request.POST['mobile']
        worker.save()
        return redirect('EditWorker')
    return render(request, 'EditWorkermobile.html')


def vieworders(request):
    """
    This function retrieves all passenger orders from the database and renders them in the 'vieworders.html' template.
    """
    context = {}
    if request.method == 'GET':
        result = models.Order.objects.all()
        context = {"result": result}
    return render(request, 'vieworders.html', context=context)


def menu(request):
    """
    This function returns the rendered template 'Menu.html'.
    """
    return render(request, 'Menu.html')


def getorder(request):
    """
    This function retrieves all passenger orders from the database and renders them in the 'Menu...html' template.
    """
    items = []
    if request.method == 'POST':
        items = request.POST.getlist('item')
        c = list(items)
        for i in range(len(c)):
            a = Order.objects.create(name=items[i])
            a.save()

        return redirect('home')
    return render(request, 'Menu.html')


def airline(request):
    
    import json

    import requests

    url = "https://skyscanner-api.p.rapidapi.com/v3/geo/hierarchy/flights/en-US"

    headers = {
        "X-RapidAPI-Key": "ca7e13dcdamsh488fef7d2d3885bp1212adjsn089ca6195eaf",
        "X-RapidAPI-Host": "skyscanner-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)
    data = response.text

    places = dict(json.loads(data)['places'])
    c = list(dict(json.loads(data)['places']).keys())
    n = {}
    for i in range(len(c)):
        n[(places[str(c[i])]['name'])] = (places[str(c[i])]['iata'])

    if request.method == 'POST':
        print('sdsfddsf')
        orgin = request.POST['from']
        destinatio = request.POST['to']
        dateD = request.POST['departure']
        dateret = request.POST['return']
        cabinclass = request.POST['search-controls-cabin-class-dropdown']
        Adultes = request.POST['adults-input']
        Children = request.POST['adults-inputa']
        l = []
        for i in range(int(Children)):
            a = random.randint(0, 15)
            l.append(a)

        print(n[orgin])
        print(n[destinatio])

        url = "https://skyscanner-api.p.rapidapi.com/v3e/flights/live/search/synced"

        payload = {"query": {
            "market": "UK",
            "locale": "en-GB",
            "currency": "EUR",
            "queryLegs": [
                {
                    "originPlaceId": {"iata": n[orgin]},
                    "destinationPlaceId": {"iata": n[destinatio]},
                    "date": {
                        "year": int(dateD[0:4]),
                        "month": int(dateD[5:7]),
                        "day": int(dateD[8:11])
                    }
                },
                {
                    "originPlaceId": {"iata": n[destinatio]},
                    "destinationPlaceId": {"iata": n[orgin]},
                    "date": {
                        "year": int(dateret[0:4]),
                        "month": int(dateret[5:7]),
                        "day": int(dateret[8:11])
                    }
                }
            ],
            "cabinClass": "CABIN_CLASS_ECONOMY",
            "adults": int(Adultes),
            "childrenAges": l
        }}
        headers = {
            "content-type": "application/json",
            "X-RapidAPI-Key": "ca7e13dcdamsh488fef7d2d3885bp1212adjsn089ca6195eaf",
            "X-RapidAPI-Host": "skyscanner-api.p.rapidapi.com"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.status_code)
        print(" ")
        data = response.json()
        a = list(dict(dict(dict(dict(data)['content'])[
                 'results'])['itineraries']).keys())
        cirr = dict(dict(dict(dict(data)['content'])['results'])['carriers'])

        dect = {}
        dec = {}

        for i in range(len(a)):
            dect[i] = dec
            dec['amount'] = dict(dict(dict(data)['content'])['results'])[
                'itineraries'][a[i]]['pricingOptions'][0]['price']['amount']
            dec['arrivalDateTimeA'] = dict(dict(dict(data)['content'])['results'])['legs'][
                dict(dict(dict(data)['content'])['results'])['itineraries'][a[i]]['legIds'][0]]['arrivalDateTime']
            dec['departureDateTimeA'] = dict(dict(dict(data)['content'])['results'])['legs'][
                dict(dict(dict(data)['content'])['results'])['itineraries'][a[i]]['legIds'][0]]['departureDateTime']
            dec['durationInMinutesA'] = dict(dict(dict(data)['content'])['results'])['legs'][
                dict(dict(dict(data)['content'])['results'])['itineraries'][a[i]]['legIds'][0]]['durationInMinutes']
            dec['arrivalDateTimeR'] = dict(dict(dict(data)['content'])['results'])['legs'][
                dict(dict(dict(data)['content'])['results'])['itineraries'][a[i]]['legIds'][1]]['arrivalDateTime']

            dec['departureDateTimeR'] = dict(dict(dict(data)['content'])['results'])['legs'][
                dict(dict(dict(data)['content'])['results'])['itineraries'][a[i]]['legIds'][1]]['departureDateTime']
            dec['durationInMinutesR'] = dict(dict(dict(data)['content'])['results'])['legs'][
                dict(dict(dict(data)['content'])['results'])['itineraries'][a[i]]['legIds'][1]]['durationInMinutes']

            dec['away'] = cirr[(dict(dict(dict(data)['content'])['results'])['legs'][
                dict(dict(dict(data)['content'])['results'])['itineraries'][a[i]]['legIds'][0]]['operatingCarrierIds'])[
                0]]
            dec['return'] = cirr[(dict(dict(dict(data)['content'])['results'])['legs'][
                dict(dict(dict(data)['content'])['results'])['itineraries'][a[i]]['legIds'][1]]['operatingCarrierIds'])[
                0]]
            dec['orgin'] = n[orgin]
            dec['destinatio'] = n[destinatio]
            dec = {}

        context = {'dct': dect}
        print(dect)
        return render(request, 'airline.html', context)
    else:
        return render(request, 'SearchFlight.html')

    # print(list(dict(json.loads(data)['content']['results']['itineraries']).keys()))


def SearchFilght(request):
    import json

    import requests

    url = "https://skyscanner-api.p.rapidapi.com/v3/geo/hierarchy/flights/en-US"

    headers = {
        "X-RapidAPI-Key": "ca7e13dcdamsh488fef7d2d3885bp1212adjsn089ca6195eaf",
        "X-RapidAPI-Host": "skyscanner-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    print(response.status_code)
    data = response.text

    places = dict(json.loads(data)['places'])
    c = list(dict(json.loads(data)['places']).keys())
    n = []
    for i in range(len(c)):
        n.append(places[str(c[i])]['name'])

    # print(d)'''

    return render(request, 'SearchFlight.html', {"places": n})


def Filght(request):
    import json
    a = {}
    if request.method == 'POST':

        a = "{" + request.POST['flight'][1:] + ""
        res = eval(a.replace("'", "\""))
        print(str(res))

        amount = float(res['amount'])
        a = int(res['arrivalDateTimeA']['year'])
        b = int(res['arrivalDateTimeA']['month'])
        c = int(res['arrivalDateTimeA']['day'])
        d = int(res['arrivalDateTimeA']['hour'])
        e = int(res['arrivalDateTimeA']['minute'])
        f = int(res['arrivalDateTimeA']['second'])

        da1 = datetime(a, b, c, d, e, f)
        da2 = datetime(int(res['departureDateTimeA']['year']), int(res['departureDateTimeA']['month']), int(
            res['departureDateTimeA']['day']), int(res['departureDateTimeA']['hour']), int(res['departureDateTimeA']['minute']))

        da3 = datetime(int(res['arrivalDateTimeR']['year']), int(res['arrivalDateTimeR']['month']),
                       int(res['arrivalDateTimeR']['day']), int(res['arrivalDateTimeR']['hour']), int(res['arrivalDateTimeR']['minute']))

        da4 = datetime(int(res['departureDateTimeR']['year']), int(res['departureDateTimeR']['month']),
                       int(res['departureDateTimeR']['day']), int(res['departureDateTimeR']['hour']), int(res['departureDateTimeR']['minute']))

        durationInMinutesA = int(res['durationInMinutesA'])
        durationInMinutesR = int(res['durationInMinutesR'])

        imgaway = res['away']['imageUrl']
        imgare = res['return']['imageUrl']
        fli = Flight.objects.create(amount=amount, arrivalDateTimeAway=da1, departureDateTimeA=da2,
                                    durationInMinutesA=durationInMinutesA,
                                    away=res['orgin'],
                                    awayimg=imgaway,
                                    arrivalDateTimeR=da3,
                                    departureDateTimeR=da4,
                                    durationInMinutesR=durationInMinutesR,
                                    returnf=res['destinatio'], returnimg=imgare)
        fli.save()
        return render(request, 'paypal.html')

    return render(request, 'airline.html')


def Table_passenger(request):
    passengers = Passenger.objects.all()
    return render(request, 'detailspassenger.html', {'passengers': passengers})


def delete_passenger(request, passenger_id):
    passenger = get_object_or_404(Passenger, id=passenger_id)
    passenger.user.delete()
    passenger.delete()
    return redirect('Table_passenger')


def Table_worker(request):
    workers = Worker.objects.all()
    return render(request, 'detailsWorker.html', {'workers': workers})


def delete_worker(request, worker_id):
    worker = Worker.objects.get(id=worker_id)
    user = worker.user
    user.delete()
    return redirect('Table_worker')
