from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth.models import User,Group
from academics.models import employee,stud_details
from outpass.models import Hostel


def unauthorized_func(view_func):
    def wrapper_func(request,*args,**kwargs):
        print(request.user)
        if request.user.is_authenticated:
            ide = employee.objects.filter(EmployeeID = request.user)
            ids = stud_details.objects.filter(UniversityEmailID=request.user.username)
            if ide:
                for i in ide:
                    id = i.Etype
                if id == "DEANSOE":
                    return redirect('/academic/deanENG')
                elif id =="DEANSOM":
                    return redirect('/academic/deanMGMT')
                elif id =="COE":
                    return redirect('/academic/COE')
                elif id== "HOD":
                    return redirect('/academic/HOD')
                elif id=="ASSISTANT-PROF":
                    return redirect('/academic/ASSTPROF')
                elif id=="REGISTRAR":
                    return redirect('/academic/registrar')
                elif id =="VICE-CHANCELLOR":
                    return redirect('/academic/vc')
            elif ids: 
                return redirect('/socrates')
            elif Group.objects.filter(user = User.objects.get(username=request.user).id):
                return redirect('/its')
            elif (Hostel.objects.filter(HostelID=request.user).exists()):
                return redirect('/outpass/Hostel_home')
            else:
                return HttpResponse('Route Does Not Exist')
        else:
            return view_func(request,*args,**kwargs)
    return wrapper_func