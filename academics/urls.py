from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path("",views.index),
    path('notice',views.notice),
    #path('notice',views.notice_index),
    #path('make',views.make),
    #path('noticeContent',views.make),
    #path('oldNotice',views.oldNotice),
    #path('<int:id>',views.rendNotice),
    path('NoticeRequest',views.NoticeRequest),
    path('Accept/<int:id>',views.Accept),
    path('Decline/<int:id>',views.Decline),
     path('home',views.home),

    #--------------MAIN ACADEMICS-------------------
    
    path('<str:id>',views.Etype),
    path('lecture/view',views.lecture),
    path('lecture/AddLecture',views.AddLecture),
    path('lecture/RemoveLecture',views.remove),
    path('test',views.test),
   
    path('department/<str:id>',views.department,name="department"),
    path('department/<str:id>/view',views.department),
    path('department/<str:id/faculty',views.DepartmentFaculty),
    path('faculty/info',views.faculty_info),

    #----------------Assistant professors--------------

    path('ASSTPROF/lecture/view',views.asstlecture),
    path('ASSTPROF/lecture/<str:lecture>/view',views.assLectureView),
    path('ASSTPROF/lecture/lectureRequest',views.lectureRequest),
    path('ASSTPROF/lecture/lectureRequestData',views.lectureRequest),
    path('ASSTPROF/lecture/lectureStatus',views.lectureStatus),
    path('ASSTPROF/lecture/<int:id>/lectureChangedData',views.lectureChangeInfo),
    path('ASSTPROF/lecture/<str:id>/Track',views.trackLecture),
    path('ASSTPROF/lecture/<str:id>/goalsInfo',views.trackLecture),

    #----------------------------- Attendance Module--------------------------------- 

    path('ASSTPROF/lecture/<str:id>/attendence',views.ProfAttendence),
    path('ASSTPROF/lecture/<str:id>/saveAttendence',views.ProfAttendence),
    path('ASSTPROF/lecture/<str:id>/ViewAttendence',views.ProfAttendenceView),


    #-----------------Head Of Department-----------------------

    path('HOD/lecture/view',views.hodLecture),
    path('HOD/lecture/lectureRequest',views.HodLectureRequest),
    path('HOD/lecture/<str:id>/update',views.lectureChangeRequest),
    path('HOD/lecture/<str:id>/Approve',views.lectureApproveRequest),
    path('HOD/lecture/<str:id>/Configure',views.lectureConfigureRequest),
    path('HOD/Outpass/requests',views.OutpassRequests),
    path('HOD/lecture/<str:id>/Enrollment',views.LectureEnrollments),
    path('HOD/lecture/<str:id>/filter',views.lectureFilter),
    path('HOD/lecture/<str:LectureID>/Enroll/<str:EnrollmentNumber>',views.LectureEnrollmentDone),
    path('HOD/lecture/<str:lecture>/view',views.lol),
    path('HOD/lecture/<str:id>/Track',views.trackLectureHod),

    #-----------------DEAN OF ENGINEERING ---------------------

    path('deanEng/lecture/view',views.deanLecture),
    path('deanEng/lecture/lectureRequest',views.DeanLectureRequest),
    path('deanEng/lecture/lectureOngoing',views.DeanOngoingRequest),
    path('deanEng/lecture/<int:id>/update',views.lectureChangeRequest),
    path('deanEng/lecture/<int:id>/Approve',views.lectureApproveRequest),
    path('deanEng/lecture/<int:id>/Configure',views.lectureConfigureRequest),

    #--------------------VICE - CHANCELLOR -----------------------

    path('vc/lecture/view',views.lectureView),
    path('vc/lecture/lectureRequest',views.vclectureRequest),
    path('vc/lecture/<int:id>/update',views.lectureChangeRequest),
    path('vc/lecture/<int:id>/Approve',views.lectureApproveVc)

   

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)