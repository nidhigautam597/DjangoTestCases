import imp
from django.shortcuts import render
from MYSQLTestCase.models import insertemprecord
from django.db import connection
from django.contrib import messages


# Create your views here.

def MySQLTestCase(request):
    if request.method=="POST":
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email'):
            empsave=insertemprecord()
            empsave.firstname=request.POST.get('firstname')
            empsave.lastname=request.POST.get('lastname')
            empsave.email=request.POST.get('email')
            cursor=connection.cursor()
            cursor.execute("call insertrecord('"+empsave.firstname+"', '"+empsave.lastname+"', '"+empsave.email+"')")
            messages.success(request,"The Employee" +empsave.firstname+" Is Saved Successfully..!")
            return render(request,'index.html')
    else:
        return render(request,'index.html')


