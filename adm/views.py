from django.core import paginator
from django.shortcuts import render
from django.utils import timezone
from datetime import date
from django.core.paginator import Paginator
from account.models import MyUser
# Create your views here.


def admin_home(request):
    return render(request, 'admin_home.html')


def total_student(request):
    all_student = MyUser.objects.all().filter(user_type=1).order_by('-id')
    p=Paginator(all_student,7)
    page_number=request.GET.get('page')
    try:
        page_obj=p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'student_table.html', context)
