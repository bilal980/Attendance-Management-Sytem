from django.urls import path
from students import views
urlpatterns = [
    path('',views.student_home,name='student_home'),
    path('attendance/',views.attendace,name='attendance'),
    path('leave/',views.leave,name='leave'),
    path('check/attendance/',views.check_attendace,name='check_attendance'),
]