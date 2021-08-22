from django.urls import path
from students import views
urlpatterns = [
    path('',views.student_home,name='student_home'),
    path('attendance/',views.attendace,name='attendance'),
    path('update/profile', views.update_profile, name='update_profile'),
    path('attendance/table',views.attendance_table,name='attendance_table'),
    path('leave/',views.leave,name='leave'),
    path('check/attendance/',views.check_attendace,name='check_attendance'),
]
