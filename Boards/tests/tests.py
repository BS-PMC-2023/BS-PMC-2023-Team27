from Boards.views import HomePageadmin, homePageWorker, LogIN, SignUpPage, SignUp, worker_signup, aboutus
from django.urls import resolve, reverse
from django.test import tag
from django.test import SimpleTestCase
from Boards.models import User
from django.test import Client, TestCase
from django.urls import reverse
from django.contrib import messages, auth
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

    def test_About_url_resolves(self):
        url = reverse('aboutus')
        self.assertEquals(resolve(url).func, aboutus)


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
        response = client.get(reverse('aboutus'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'aboutus.html')

    @tag('integration-test')
    def test_admin_login_and_logout(self):
        """test_login_and_logout """

        # print(a.username)
        data = {'username': 'yehia', 'password': '123'}
        response = self.client.post(reverse('home'), data=data, follow=True)
        a = self.assertEqual(response.status_code, 200)

        value = 'Login.html'
        self.assertTrue(response, value)

        response = self.client.get(reverse('logout'), follow=True)

        # Assert
        c = self.assertNotEqual(response.status_code, 300)
        self.assertFalse(response.context["user"].is_authenticated)

    @tag('integration-test')
    def test_Passenger_login_and_logout(self):
        """test_login_and_logout """

        # print(a.username)
        data = {'username': 'ppp', 'password': 'Pp123456789+'}
        response = self.client.post(reverse('home'), data=data, follow=True)
        a = self.assertEqual(response.status_code, 200)

        value = 'Login.html'
        self.assertTrue(response, value)

        response = self.client.get(reverse('logout'), follow=True)

        # Assert
        c = self.assertNotEqual(response.status_code, 300)
        self.assertFalse(response.context["user"].is_authenticated)

    @tag('integration-test')
    def test_Worker_login_and_logout(self):
        """test_login_and_logout """

        # print(a.username)
        data = {'username': 'nnn', 'password': '1234'}
        response = self.client.post(reverse('home'), data=data, follow=True)
        a = self.assertEqual(response.status_code, 200)

        value = 'Login.html'
        self.assertTrue(response, value)

        response = self.client.get(reverse('logout'), follow=True)

        # Assert
        c = self.assertNotEqual(response.status_code, 300)
        self.assertFalse(response.context["user"].is_authenticated)

    @tag('integration-test')
    def test_add_to_worker_list(self):
        """"""
        # accss view
        response = self.client.get(('login'))
        a = self.assertTrue(User.is_authenticated)

        response = self.client.get(('SignUpPage'))
        b = self.assertNotEqual(response.status_code, 300)

        response = self.client.get(('homePage'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)

    @tag('integration-test')
    def test_Passenger_about(self):
        """"""
        # accss view
        response = self.client.get(('login'))
        a = self.assertTrue(User.is_authenticated)

        response = self.client.get(('aboutus'))
        b = self.assertNotEqual(response.status_code, 300)

        response = self.client.get(('homePage'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)

    @tag('integration-test')
    def test_Search_f_(self):
        response = self.client.get(('login'))
        a = self.assertTrue(User.is_authenticated)

        response = self.client.get(('SearchFilght'))
        b = self.assertNotEqual(response.status_code, 300)

        response = self.client.get(('homePage'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)

    @tag('integration-test')
    def test_Search_f_(self):
        response = self.client.get(('login'))
        a = self.assertTrue(User.is_authenticated)

        response = self.client.get(('menu'))
        b = self.assertNotEqual(response.status_code, 300)

        response = self.client.get(('homePage'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)


@tag("unit_test")
class Test_forms(TestCase):
    @tag('unit-test')
    def test_user_form(self):

        form = WorkerUserForm(data={
            'first_name': '',
            'last_name': '',
            'username': '',
            'password': '', })
        form1 = WorkerForm(data={
            'mobile': '',
            'profile_pic': '',
            'id_user': ''
        })
        self.assertFalse(form.is_valid())

        self.assertFalse(form1.is_valid())

    # def test_Passenger_form(self):


@tag('integration-test')
class Test_integ(TestCase):

    @tag('integration-test')
    def test_admin_login_and_logout(self):
        """test_login_and_logout """

        # print(a.username)
        data = {'username': 'yehia', 'password': '123'}
        response = self.client.post(reverse('home'), data=data, follow=True)
        a = self.assertEqual(response.status_code, 200)

        value = 'Login.html'
        self.assertTrue(response, value)

        response = self.client.get(reverse('logout'), follow=True)

        # Assert
        c = self.assertNotEqual(response.status_code, 300)
        self.assertFalse(response.context["user"].is_authenticated)

    @tag('integration-test')
    def test_Passenger_login_and_logout(self):
        """test_login_and_logout """

        # print(a.username)
        data = {'username': 'ppp', 'password': 'Pp123456789+'}
        response = self.client.post(reverse('home'), data=data, follow=True)
        a = self.assertEqual(response.status_code, 200)

        value = 'Login.html'
        self.assertTrue(response, value)

        response = self.client.get(reverse('logout'), follow=True)

        # Assert
        c = self.assertNotEqual(response.status_code, 300)
        self.assertFalse(response.context["user"].is_authenticated)

    @tag('integration-test')
    def test_Worker_login_and_logout(self):
        """test_login_and_logout """

        # print(a.username)
        data = {'username': 'nnn', 'password': '1234'}
        response = self.client.post(reverse('home'), data=data, follow=True)
        a = self.assertEqual(response.status_code, 200)

        value = 'Login.html'
        self.assertTrue(response, value)

        response = self.client.get(reverse('logout'), follow=True)

        # Assert
        c = self.assertNotEqual(response.status_code, 300)
        self.assertFalse(response.context["user"].is_authenticated)

    @tag('integration-test')
    def test_add_to_worker_list(self):
        """"""
        # accss view
        response = self.client.get(('login'))
        a = self.assertTrue(User.is_authenticated)

        response = self.client.get(('SignUpPage'))
        b = self.assertNotEqual(response.status_code, 300)

        response = self.client.get(('homePage'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)

    @tag('integration-test')
    def test_Passenger_about(self):
        """"""
        # accss view
        response = self.client.get(('login'))
        a = self.assertTrue(User.is_authenticated)

        response = self.client.get(('aboutus'))
        b = self.assertNotEqual(response.status_code, 300)

        response = self.client.get(('homePage'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)

    @tag('integration-test')
    def test_Search_f_(self):
        response = self.client.get(('login'))
        a = self.assertTrue(User.is_authenticated)

        response = self.client.get(('SearchFilght'))
        b = self.assertNotEqual(response.status_code, 300)

        response = self.client.get(('homePage'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)

    @tag('integration-test')
    def test_Search_f_(self):
        response = self.client.get(('login'))
        a = self.assertTrue(User.is_authenticated)

        response = self.client.get(('menu'))
        b = self.assertNotEqual(response.status_code, 300)

        response = self.client.get(('homePage'))
        self.assertNotEqual(response.status_code, 300)

        response = self.client.get(reverse('logout'), follow=True)

        self.assertEqual(response.status_code, 200)
