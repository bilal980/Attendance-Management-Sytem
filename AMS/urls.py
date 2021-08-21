
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('index/', views.index, name='index'),
]
