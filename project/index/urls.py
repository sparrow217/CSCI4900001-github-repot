
from django.conf.urls import url
from .views import *

urlpatterns = [
	url('', IndexView.as_view())
]