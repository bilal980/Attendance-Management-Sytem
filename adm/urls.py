from typing import Pattern
from django.urls import path
from adm.views import admin_home
urlpatterns = [
    path('',admin_home,name='admin_home'),
]
