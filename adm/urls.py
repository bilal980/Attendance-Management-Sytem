
from django.urls import path
from adm import views

urlpatterns = [
    path('',views.admin_home,name='admin_home'),
    path('total/students',views.total_student,name='total_student'),
    path('student/attendance/<int:pk>',views.students_attendance,name='students_attendance'),
    path('student/deleted/<int:pk>', views.delete_student, name='delete_student'),
    path('add/attendance/<int:pk>', views.add_attendance, name='add_attendance'),
    path('update/attendance/<int:pk>',views.update_attendance,name='update_attendance'),
    path('delete/attendance/<int:pk>',views.delete_attendance,name='delete_attendance'),
    path('leave/approvel/', views.leave_approvel, name='leave_approvel'),
    path('leave/approvel/<int:pk>/<int:val>', views.leave_approvel_response, name='leave_approvel_response'),
    path('report/<int:pk>',views.report,name='report'),
    path('fetch/record',views.fetch_record,name='fetch_record'),
    path('complete/record', views.complete_report, name='complete_report'),
    path('grade/', views.grade, name='grade'),
]
