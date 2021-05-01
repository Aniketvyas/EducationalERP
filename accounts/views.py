from django.shortcuts import render , redirect 
from django.contrib.auth.models import User , auth , Group
from django.http import HttpResponse
from outpass.models import stud_outing ,Warden ,  stud_board , Hostel
from django.contrib import messages
from . import models
import datetime as dt
from datetime import *
import random
from django.shortcuts import get_object_or_404  
from django.contrib.auth.decorators import login_required
from academics.models import employee , stud_details

from .decorators import unauthorized_func

# Create your views here.


#-----------------------------Login Logout-----------------------------------------#



@unauthorized_func
def login(request):
    print('login')
    if request.method=='POST':
        username = request.POST['email']
        password = request.POST['Password']
        user = auth.authenticate(username=username,password=password)
        a = employee.objects.filter(EmployeeID=username)
        for i in a:
            a = i.Etype
            print("a",a)
        print(user , username,password)
        # print(type(Group.objects.get(user=User.objects.get(username=username))),Group.objects.get(user=User.objects.get(username=username)) == "guard")
        if user is not None:
            print(user)
            if (stud_details.objects.filter(UniversityEmailID=username).exists()):
                auth.login(request,user)
                return redirect('/socrates',)
            elif (Warden.objects.filter(wardenID=username).exists()):
                auth.login(request , user)
                return redirect('/outpass/warden_home')
            elif (Hostel.objects.filter(HostelID=username).exists()):
                auth.login(request,user)
                return redirect('/outpass/Hostel_home')
            elif (Group.objects.filter(user = User.objects.get(username=username).id)=='its'):
                auth.login(request,user)
                return redirect('/its')
            elif ("guard" in Group.objects.filter(user=User.objects.get(username=username))):
                auth.login(request,user)
                return redirect('/outpass/gate')
            elif a:
                if a=="REGISTRAR":
                    auth.login(request,user)
                    return redirect('/academic/registrar')
                elif a=='DEANSOE':
                    auth.login(request,user)
                    return redirect('/academic/deanENG')
                elif a=='DEANSOM':
                    auth.login(request,user)
                    return redirect('/academic/deanMGMT')
                elif a=="HOD":
                    auth.login(request,user)
                    return redirect('/academic/hod')
                elif a=="COE":
                    auth.login(request,user)
                    return redirect('/academic/COE')
                elif a=="ASSISTANT-PROF":
                    auth.login(request,user)
                    return redirect('/academic/ASSTPROF')
                elif a == 'VICE-CHANCELLOR':
                    auth.login(request,user)
                    return redirect('/academic/vc')
                else:
                    return HttpResponse('ERROR 404')
            else:
                a= Warden.objects.filter(wardenID=username)
                if a:
                    return redirect('/warden_home')
                else:
                    return HttpResponse(request,'page not found')
        else:
            messages.info(request,'Invalid credentials') 
            return redirect('/')   
    else:
        return render(request,'index.html')    




def logout(request):
    auth.logout(request)
    return redirect('/')
    