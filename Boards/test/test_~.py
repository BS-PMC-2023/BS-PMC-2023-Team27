from django.test import TestCase,SimpleTestCase
import  unittest
from django.test import tag
from django.urls import resolve,reverse



@tag("unit_test")
class TestUrls(SimpleTestCase):
    def Test_HomePageadmin_url_resolves(self):
        url=reverse('HomePageadmin')
        self.assrtEquals(resolve(url).func,HomePageadmin)

    def Test_homePageWorker_url_resolves(self):
        url=reverse('homePageWorker')
        self.assrtEquals(resolve(url).func,homePageWorker)

    def Test_Home_url_resolves(self):
        url=reverse('homePage')
        self.assrtEquals(resolve(url).func,homePage)
    def Test_SignUp_url_resolves(self):
        url=reverse('SignUp')
        self.assrtEquals(resolve(url).func,SignUp)