from rest_framework import serializers
from .models import *

class DepartSerilizer(serializers.ModelSerializer):
    class Meta:
        model = deparment
        fields = ['name']
        # fields = '__all__'
class EmployeeSerilizer(serializers.ModelSerializer):    
    deparment_name = DepartSerilizer()
    class Meta:
        model = employee
        fields = ['name','deparment_name']
        # fields = '__all__'
        # exclude=['id']