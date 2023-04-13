# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from .views import *

urlpatterns = [

    # The home page
    path('', index, name='home'),
    path('test', test, name='test'),

    # Matches any html file
    #re_path(r'^.*\.*', views.pages, name='pages'),

]
