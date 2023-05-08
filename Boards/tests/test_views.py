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


class TestViews(TestCase):

    def Homeview(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'index.html')
