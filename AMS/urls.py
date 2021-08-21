
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('register/', views.register, name='register'),
    path('adm/',include('adm.urls')),
    path('student/',include('students.urls')),
]
