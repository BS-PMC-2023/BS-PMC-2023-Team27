from django.test import TestCase
import  unittest
from django.test import tag
from django.urls import resolve,reverse
from Boards import views

@tag("unit_test")
class TestUrls(SimpleTestCase):
    def Test_HomePageadmin_url_resolves(self):
        url=reverse('HomePageadmin')
        self.assrtEquals(resolve(url).func,HomePageadmin)

