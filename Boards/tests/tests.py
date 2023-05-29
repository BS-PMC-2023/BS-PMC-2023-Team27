from Boards.views import ContactUs, EditWorker, EditWorkerEmail, EditWorkerIDuser, EditWorkermobile, EditWorkerusername, HomePageadmin, aboutus, homePageWorker, LogIN, SignUpPage, SignUp, viewAllReports, worker_signup, about, workersReport
from django.urls import resolve, reverse
from django.test import tag
from django.test import SimpleTestCase
from Boards.models import User
from django.test import Client, TestCase
from django.urls import reverse
import unittest
import json
from Boards.models import Worker, Passenger, User
from Boards.forms import WorkerUserForm, WorkerForm


@tag('unit-test')
class TestUrls(SimpleTestCase):

    def test_homepageadmin_url_resolves(self):
        url = reverse('HomePageadmin')
        self.assertEquals(resolve(url).func, HomePageadmin)

    def test_homePageWorker_url_resolves(self):
        url = reverse('homePageWorker')
        self.assertEquals(resolve(url).func, homePageWorker)

    def test_SignUp_url_resolves(self):
        url = reverse('SignUp')
        self.assertEquals(resolve(url).func, SignUp)

    def test_SignUpPage_url_resolves(self):
        url = reverse('SignUpPage')
        self.assertEquals(resolve(url).func, SignUpPage)

    def test_LogIN_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, LogIN)

    def test_worker_signup_url_resolves(self):
        url = reverse('worker_signup')
        self.assertEquals(resolve(url).func, worker_signup)

    def test_aboutus_url_resolves(self):
        url = reverse('aboutus')
        self.assertEquals(resolve(url).func, aboutus)
    
    def test_ContactUs_url_resolves(self):
        url = reverse('ContactUs')
        self.assertEquals(resolve(url).func, ContactUs)
    
    def test_workerreport_url_resolves(self):
        url = reverse('workerreport')
        self.assertEquals(resolve(url).func, workersReport)
    
    def test_viewAllReports_url_resolves(self):
        url = reverse('viewAllReports')
        self.assertEquals(resolve(url).func, viewAllReports)
    
    def test_EditWorker_url_resolves(self):
        url = reverse('EditWorker')
        self.assertEquals(resolve(url).func, EditWorker)
    
    def test_EditWorkerusername_url_resolves(self):
        url = reverse('EditWorkerusername')
        self.assertEquals(resolve(url).func, EditWorkerusername)
    
    def test_EditWorkerIDuser_url_resolves(self):
        url = reverse('EditWorkerIDuser')
        self.assertEquals(resolve(url).func, EditWorkerIDuser)
    
    def test_EditWorkerEmail_url_resolves(self):
        url = reverse('EditWorkerEmail')
        self.assertEquals(resolve(url).func, EditWorkerEmail)
    
    def test_EditWorkermobile_url_resolves(self):
        url = reverse('EditWorkermobile')
        self.assertEquals(resolve(url).func, EditWorkermobile)

   


@tag('unit-test')
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.Homeurl = reverse('home')
        self.homwpaurl = reverse('homePage')

    @tag('unit-test')
    def test_homepage_view(self):
        client = Client()
        response = client.get(self.homwpaurl)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    @tag('unit-test')
    def test_Home_view(self): '''
        client = Client()
        response = client.get(self.Homeurl)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogIn.html')

    def test_logout_view(self):
        client = Client()
        response = client.get(reverse('logout'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'LogIn.html')'''

    @tag('unit-test')
    def test_HomePageadmin_view(self):
        client = Client()
        response = client.get(reverse('HomePageadmin'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HomePageadmin.html')

    @tag('unit-test')
    def test_homePageWorker_view(self):
        client = Client()
        response = client.get(reverse('homePageWorker'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'homePageWorker.html')

    @tag('unit-test')
    def test_Sign_up_view(self):
        client = Client()
        response = client.get(reverse('SignUp'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'SignUp.html')

    @tag('unit-test')
    def test_SignUpPage_view(self):
        client = Client()
        response = client.get(reverse('SignUpPage'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'SignUp.html')

    @tag('unit-test')
    def test_SignUpPage_view(self):
        client = Client()
        response = client.get(reverse('worker_signup'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'workersignup.html')

    @tag('unit-test')
    def test_About_view(self):
        client = Client()
        response = client.get(reverse('About'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus.html')
    
    @tag('unit-test')
    def test_ContactUs_view(self):
        client = Client()
        response = client.get(reverse('ContactUs'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'ContactUs.html')    
    
    @tag('unit-test')
    def test_workerreport_view(self):
        client = Client()
        response = client.get(reverse('workerreport'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'workerreport.html')
    
    
    @tag('unit-test')
    def test_viewAllReports_view(self):
        client = Client()
        response = client.get(reverse('viewAllReports'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewAllReports.html')
    
    
    @tag('unit-test')
    def test_EditWorker_view(self):
        client = Client()
        response = client.get(reverse('EditWorker'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'EditWorker.html')

    
    
    @tag('unit-test')
    def test_EditWorkerusername_view(self):
        client = Client()
        response = client.get(reverse('EditWorkerusername'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'EditWorkerusername.html')

    
    
    @tag('unit-test')
    def test_EditWorkerIDuser_view(self):
        client = Client()
        response = client.get(reverse('EditWorkerIDuser'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'EditWorkerIDuser.html')
    
    
    @tag('unit-test')
    def test_EditWorkerEmail_view(self):
        client = Client()
        response = client.get(reverse('EditWorkerEmail'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'EditWorkerEmail.html')
    
    
    @tag('unit-test')
    def test_EditWorkermobile_view(self):
        client = Client()
        response = client.get(reverse('EditWorkermobile'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'EditWorkermobile.html')




@tag("unit_test")
class Test_forms(TestCase):
    @tag('unit-test')
    def test_user_form(self):

        form = WorkerUserForm(data={
            'first_name': 'sadsd',
            'last_name': 'dsfsfs',
            'username': 'Pp',
            'password': 'Pp123456789=+', })
        form1 = WorkerForm(data={
            'mobile': '877645',
            'profile_pic': '',
            'id_user': '976657'
        })
        self.assertTrue(form.is_valid())

        self.assertTrue(form1.is_valid())

    # def test_Passenger_form(self):
