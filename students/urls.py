from django.urls import path
from students import views
urlpatterns = [
    path('',views.student_home,name='student_home')
]