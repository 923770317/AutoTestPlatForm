# -*- coding: utf-8 -*-
from django.conf.urls import url
import views



import views

urlpatterns = [url(r'^$', views.index),
               url(r'^send/$', views.sendRequest),
               url(r'^save/$', views.saveRequest),
               ]
