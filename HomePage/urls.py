from django.conf.urls import *
from . import views

urlpatterns = [url(r'^$', views.HomePage, name='HomePage'),
]
