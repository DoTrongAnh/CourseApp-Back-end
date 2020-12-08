# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 17:57:52 2020

@author: anhtr
"""


from django.urls import path, include
'''
from views import EchoViewSet
from rest_framework import renderers
'''
from rest_framework.routers import DefaultRouter
from . import views

'''
echo_list = EchoViewSet.as_view({
    'get':'list',
    'post':'create'
    })

echo_details = EchoViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
    })

echo_highlight = EchoViewSet.as_view({
    'get':'hightlight'
    }, renderer_classes=[renderers.StaticHTMLRenderer])
'''
router = DefaultRouter()
router.register(r'echos', views.EchoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]