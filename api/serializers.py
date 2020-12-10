# -*- coding: utf-8 -*-
"""
Created on Sun Dec  6 18:10:30 2020

@author: anhtr
"""


from rest_framework import serializers
from api.models import Echo

class EchoSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Echo
        fields = ['id', 'message', 'created']
