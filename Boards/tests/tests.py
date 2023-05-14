from Boards.views import HomePageadmin, homePageWorker, LogIN, SignUpPage, SignUp, worker_signup, about
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


@tag("unit_test")
class TestUrls(SimpleTestCase):

    @tag('unit-test')
    def test_homepageadmin_url_resolves(self):
        url = reverse('HomePageadmin')
        self.assertEquals(resolve(url).func, HomePageadmin)

    @tag('unit-test')
    def test_homePageWorker_url_resolves(self):
        url = reverse('homePageWorker')
        self.assertEquals(resolve(url).func, homePageWorker)

    @tag('unit-test')
    def test_SignUp_url_resolves(self):
        url = reverse('SignUp')
        self.assertEquals(resolve(url).func, SignUp)

    @tag('unit-test')
    def test_SignUpPage_url_resolves(self):
        url = reverse('SignUpPage')
        self.assertEquals(resolve(url).func, SignUpPage)

    @tag('unit-test')
    def test_LogIN_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, LogIN)

    @tag('unit-test')
    def test_worker_signup_url_resolves(self):
        url = reverse('worker_signup')
        self.assertEquals(resolve(url).func, worker_signup)

    @tag('unit-test')
    def test_About_url_resolves(self):
        url = reverse('About')
        self.assertEquals(resolve(url).func, about)


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


@tag("unit_test")
class Test_forms(TestCase):

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
