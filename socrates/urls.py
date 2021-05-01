from django.urls import path
from . import views

urlpatterns = [
    path('',views.Home),
    path('outing',views.outing),
    path('attendance',views.studentAttendanceView),
    path('lecture',views.lecture),
    path('<str:lecture>/Track',views.track)
]