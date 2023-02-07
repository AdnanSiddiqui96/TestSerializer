from django.shortcuts import render
import datetime
from datetime import datetime, timedelta
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import F, Q
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.views import APIView
from rest_framework import generics
from .serializer import*
from .models import *
from django.db.models import F
import random


class depart(APIView):
    def post(self,request):
        name = request.data.get('name')
        data = deparment(name = name)
        dep = deparment.objects.values()
        data.save()
        return Response({'status':True,'message':'A new department added successfully.','Data':dep})
    def get(self,request):
        dep =  deparment.objects.all()
        depmt = DepartSerilizer(dep,many = True).data
        return Response({'status':True,'Data':depmt})
class employees(APIView):
    def post(self,request):
        name = request.data.get('name')
        city = request.data.get('city')
        deparment_name = request.data.get('deparment_name')
        objDep = deparment.objects.filter(name = deparment_name).first()
        emp = employee(name = name,city = city,deparment_name = objDep)
        empData = employee.objects.values(Name=F('name'),Department=F('deparment_name__name'))
        emp.save()
        return Response({'status':True,'Message':'A new Employee added successfully.','Record':empData})
    def get(self,request):
        # dep = deparment.objects.filter()
        emp = employee.objects.all()       
        emply = EmployeeSerilizer(emp,many = True).data
        return Response({'status':True,'Record':emply})
    