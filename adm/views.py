from django.core import paginator
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.utils import timezone
from django.views.generic import UpdateView
from django.contrib import messages
from django.core.paginator import Paginator
from students.models import Attendance, Leave
from account.models import MyUser
from students.models import Attendance
# Create your views here.



def admin_home(request):
    return render(request, 'admin_home.html')


def total_student(request):
    all_student = MyUser.objects.all().filter(user_type=1).order_by('-id')
    p = Paginator(all_student, 7)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'student_table.html', context)


def students_attendance(request, pk):
    stu_attend = Attendance.objects.all().filter(student=pk).order_by('-id')
    student_name = MyUser.objects.get(id=pk)
    p = Paginator(stu_attend, 7)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj,
               'name': student_name.first_name, 'student_id': student_name.id}
    return render(request, 'attendance_tablel.html', context)


def update_attendance(request,pk):
    if request.method=='POST':
        try:
            att=Attendance.objects.get(id=pk)
            att.date=timezone.datetime.strptime(request.POST.get('date'), "%d-%m-%Y").date()
            att.save()
            if request.POST.get('attendance') == 'on':
                att.mark_attendance=True
                att.save()
            else:
                att.mark_attendance=False
                att.save()
            messages.success(request,'Updated Successfully!')
        except:
            messages.error('Something Wrong !')   
    up=Attendance.objects.get(id=pk)    
    return render(request,'update_attendance.html',{'obj':up,'date':up.date})

def delete_attendance(request,pk):
    try:
        Attendance.objects.get(id=pk).delete()
        messages.warning(request,"Attendance Deleted!")
    except:
        messages.error(request,'Error Occured')
    return redirect(request.META['HTTP_REFERER'])

def add_attendance(request,pk):
    student=MyUser.objects.get(id=pk)
    if request.method=="POST":
        try:
            if request.POST.get('attendance')=='on':
                att=True
            else:
                att=False
            new_att=Attendance.objects.create(date=request.POST.get('date'), student=MyUser.objects.get(id=pk), mark_attendance=att)
            new_att.save()
            messages.success(request,'Attendance Saved!')
            return redirect(request.META['HTTP_REFERER'])
        except:
            messages.error(request,'Eror!')
            return redirect(request.META['HTTP_REFERER'])
    return render(request,'add_attendance.html',{'student':student})


def delete_student(request, pk):
    try:
        MyUser.objects.get(id=pk).delete()
        messages.warning(request, "Student Deleted!")
    except:
        messages.error(request, 'Error Occured')
    return redirect(request.META['HTTP_REFERER'])


def leave_approvel(request):

    all_leave=Leave.objects.all().order_by('-id')
    p = Paginator(all_leave, 7)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
    context = {'page_obj': page_obj}
    return render(request, 'leave_approvel.html', context)

def leave_approvel_response(request,pk,val):
    appr=Leave.objects.get(id=pk)
    if val==1:
        appr.approve=True
        appr.save()
    else:
        appr.approve=False
        appr.save()
    return redirect(request.META['HTTP_REFERER'])



