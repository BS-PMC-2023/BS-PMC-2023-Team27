'''TestFile'''

from django.test import TestCase, Client
import json
from datetime import datetime
from Boards.forms import WorkerUserForm, WorkerForm
from Boards.models import Worker, Passenger, User
from django.contrib.auth.views import LogoutView
from Boards import views
from Boards.forms import WorkerUserForm, WorkerForm, PassengerUserForm, PassengerForm, ContactUsForm, WorkerReportForm
from django.test import TestCase
from django.urls import reverse
from django.test import Client, TestCase
from Boards.models import User, Worker
from django.test import SimpleTestCase
from django.test import tag
from django.urls import resolve, reverse
from Boards.views import HomePageadmin, homePageWorker, LogIN, SignUpPage, SignUp, worker_signup, aboutus, homePage, HomePageadmin, paypal, ContactUs, Contact, EditWorker, EditWorkerusername, EditWorkerIDuser, EditWorkerEmail, EditWorkermobile, airline, SearchFilght, menu, getorder, Filght, vieworders, Table_worker, Table_passenger
from Boards.models import Order


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

    def test_homepage_url_resolves(self):
        url = reverse('homePage')
        self.assertEquals(resolve(url).func, homePage)

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

    def test_Pay_url_resolves(self):
        url = reverse('paypal')
        self.assertEquals(resolve(url).func, paypal)

    def test_ContactUs_url_resolves(self):
        url = reverse('ContactUs')
        self.assertEquals(resolve(url).func, ContactUs)

    # def test_EditWorkerusername_url_resolves(self):
        # url = reverse('EditWorkerusername')
        # self.assertEquals(resolve(url).func, EditWorkerusername)

    # def test_EditWorkerusername_url_resolves(self):
        # url = reverse('EditWorkerusername')
        # self.assertEquals(resolve(url).func, EditWorkerusername)

    def test_airline_url_resolves(self):
        url = reverse('airline')
        self.assertEquals(resolve(url).func, airline)

    def test_SearchFilght_url_resolves(self):
        url = reverse('SearchFilght')
        self.assertEquals(resolve(url).func, SearchFilght)

    def test_menu_url_resolves(self):
        url = reverse('menu')
        self.assertEquals(resolve(url).func, menu)

    def test_getorder_url_resolves(self):
        url = reverse('getorder')
        self.assertEquals(resolve(url).func, getorder)

    def test_getorder_url_resolves(self):
        url = reverse('Filght')
        self.assertEquals(resolve(url).func, Filght)

    def test_Table_Worker_url_resolves(self):
        url = reverse('Table_Worker')
        self.assertEquals(resolve(url).func, Table_worker)

    def test_Table_Worker_url_resolves(self):
        url = reverse('vieworders')
        self.assertEquals(resolve(url).func, vieworders)


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
    '''
    @tag('unit-test')
    def test_Home_view(self):
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

    @tag('unit-test')
    def test_paypal(self):
        response = self.client.get(reverse('paypal'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'paypal.html')

    @tag('unit-test')
    def test_ContactUs(self):
        response = self.client.get(reverse('ContactUs'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ContactUs.html')

    @tag('unit-test')
    def test_ContactUs_post(self):
        response = self.client.post(reverse('ContactUs'), {
                                    'email': 'test@example.com', 'subject': 'Test Subject', 'Discrbition': 'Test Description'})
        # Assuming you're redirecting to 'homePage' on successful form submission
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('homePage'))

    def test_Contact(self):
        response = self.client.get(reverse('Contact'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ContactUs.html')

    def test_workersReport(self):
        response = self.client.get(reverse('workersReport'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'workerreport.html')

    '''def test_workersReport_post(self):
        # Replace field1 and field2 with the actual field names from your form
        response = self.client.post(reverse('workersReport'), {
                                    'field1': 'value1', 'field2': 'value2'})
        # Assuming you're redirecting to 'homePageWorker' on successful form submission
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('homePageWorker'))'''

    def test_viewAllReports(self):
        response = self.client.get(reverse('viewAllReports'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'viewAllReports.html')
        # Add more assertions to test the context and data displayed in the template if needed

    def test_EditWorker(self):
        response = self.client.get(reverse('EditWorker'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'EditWorker.html')
        # Add more assertions to test the context and data displayed in the template if needed

    '''def test_menu(self):
        response = self.client.get(reverse('menu'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'Menu.html')'''

    def test_vieworders(self):
        # Create some sample orders for testing
        Order.objects.create(name='Chocolate Muffin + Espresso illy')
        Order.objects.create(name='Meal Deal: Lasagna Bolognese + Soft Drink')
        Order.objects.create(name='Chicken rice + Soft Drink')

        response = self.client.get(reverse('vieworders'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vieworders.html')

        # Add more assertions to test the context and rendered data if needed

    def test_getorder(self):
        # Prepare the data for the POST request
        data = {'item': ['Chocolate Muffin + Espresso illy',
                         'Chicken rice + Soft Drink', 'Meal Deal: Lasagna Bolognese + Soft Drink']}

        response = self.client.post(reverse('getorder'), data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('HomePageadmin'))

        # Assert that the orders have been created
        orders = Order.objects.all()
        self.assertEqual(orders.count(), 3)


class SearchFlightViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Replace 'SearchFilght' with the correct URL pattern name
        self.url = reverse('SearchFilght')

    def test_search_flight_view(self):
        # Send a GET request to the view
        response = self.client.get(self.url)

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Add more assertions to validate the response content or any other expected behavior of the view

    '''def test_EditWorkerusername(self):
        # Create a worker object for testing
        # Assuming 'id_user' is the required field
        worker = Worker.objects.create(id_user=1)
        response = self.client.post(reverse('EditWorkerusername', args=[
                                    worker.user_id]), {'username': 'new_username'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('EditWorker'))'''

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
