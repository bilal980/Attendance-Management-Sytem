from typing import Pattern
from django.urls import path
from adm import views
urlpatterns = [
    path('',views.admin_home,name='admin_home'),
    path('total/students',views.total_student,name='total_student'),
]
