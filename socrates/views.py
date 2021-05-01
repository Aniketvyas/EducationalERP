from django.shortcuts import render,redirect
from academics.models import *
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
# Create your views here.
import json


def Home(request):
    print(request.user.get_username())
    return render(request, 'student/dashboard.html' )

def outing(request):
    return redirect('outpass/makeRequest')


def studentAttendanceView(request):
    name = stud_details.objects.get(UniversityEmailID=request.user)
    details = lectureEnrollment.objects.filter(studentID=name.id)
    studentDictionary={}
    dicto={}
    for i in details:
        try:
            a=attendence.objects.get(LectureID=lectures.objects.get(LectureID=i.lectureId))
        except:
            continue
        try:
            a=attendence.objects.get(LectureID=lectures.objects.get(LectureID=i.lectureId)).attendanceFile
            f = open("media/"+str(a),'r')
            y=json.load(f)
            f.close()
            arr= y['Attendance']
            r=0
            t=0
            lectureName = lectures.objects.get(LectureID=i.lectureId).LectureName
            dicto[lectureName] = len(arr.keys())
            i=1
            studentDictionary[lectureName]=0
            print(name.id)
            for r in arr.keys():
                #print(i,arr.keys(),lectureName,arr[r])
                print(name.id, arr[r])
                if name.id in arr[r]:
                    studentDictionary[lectureName]+=1
                else:
                    print('else')
                    

                i+=1
        except ObjectDoesNotExist:
            return HttpResponse('Error Occured..!!!')
    print(studentDictionary)
    main_list=[]

    print(dicto)
    j=[]
    for i in studentDictionary.keys():
        k = studentDictionary[i]
        j.append((k/dicto[i])*100)
        print((k/dicto[i])*100)

        l={"name":i,"percentage":(k/dicto[i])*100}
        main_list.append(l)
    print(main_list)
    return render(request,'student/dashboard.html',{'data':j,'labels':list(studentDictionary.keys()),"analysis":True})




def lecture(request):
    lectures = lectureEnrollment.objects.filter(studentID = stud_details.objects.get(UniversityEmailID=request.user))
    return render(request,'student/lecture.html',{'lecture':lectures})


def track(request,lecture):
    obj = lectureRecord.objects.filter(lectureId=lectures.objects.get(LectureID=lecture))
    return render(request,'bs4_Horizontal_timeline.html',{'track':obj,'student':True})