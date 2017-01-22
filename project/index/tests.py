from django.test import TestCase, Client
from .views import *
from .forms import *

class IndexViewTest(TestCase):
	client = None#Use self to refer to the class member in instance methods.

	def setUp(self):
		"""Ran before every test."""
		self.client = Client()

	def test_view_init(self):
		"""Quick and simple test to prove the view is initialized with the correct template."""
		res = self.client.get("")
		self.assertEquals(IndexView.template_name, "index.html")
		self.assertEquals(res.status_code, 200)
		self.assertTrue(isinstance(res.context['form'], IndexForm))
		#Python 3 changed the way strings and bytes work. The `b` here converts the string to bytes.
		self.assertTrue(b"Hello World" in res.content)