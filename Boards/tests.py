from django.test import SimpleTestCase
from unittest import TestCase
from django.test import tag
from django.urls import resolve,reverse
from Boards import views 



class TestUrls(SimpleTestCase):
    def test_homepageadmin_url_resolves(self):
        url=reverse('HomePageadmin')
        print(resolve(url))
        self.assrtEquals(resolve(url).func ,HomePageadmin)

    def test_homePageWorker_url_resolves(self):
        url=reverse('homePageWorker')
        self.assrtEquals(resolve(url).func,homePageWorker)


    def test_SignUp_url_resolves(self):
        url=reverse('SignUp')
        self.assrtEquals(resolve(url).func,SignUp)

    def test_SignUpPage_url_resolves(self):
        url = reverse('SignUpPage')
        self.assrtEquals(resolve(url).func, SignUpPage)

    def test_LogIN_url_resolves(self):
        url = reverse('home')
        self.assrtEquals(resolve(url).func, LogIN)