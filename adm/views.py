from django.core import paginator
from django.db.models import Q
from django.http import request
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
    all_student = MyUser.objects.all().filter(user_type=1).count()
    present = Attendance.objects.all().filter(
        mark_attendance=True, date=timezone.datetime.today()).count()
    absent = Attendance.objects.all().filter(
        mark_attendance=False, date=timezone.datetime.today()).count()
    total_leave = Leave.objects.all().filter(
        approve=True, date=timezone.datetime.today()).count()
    context = {
        'all_student': all_student,
        'present': present,
        'absent': absent,
        'total_leave': total_leave,
    }
    return render(request, 'admin_home.html', context)


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


def update_attendance(request, pk):
    if request.method == 'POST':
        try:
            att = Attendance.objects.get(id=pk)
            att.date = timezone.datetime.strptime(
                request.POST.get('date'), "%d-%m-%Y").date()
            att.save()
            if request.POST.get('attendance') == 'on':
                att.mark_attendance = True
                att.save()
            else:
                att.mark_attendance = False
                att.save()
            messages.success(request, 'Updated Successfully!')
        except:
            messages.error('Something Wrong !')
    up = Attendance.objects.get(id=pk)
    return render(request, 'update_attendance.html', {'obj': up, 'date': up.date})


def delete_attendance(request, pk):
    try:
        Attendance.objects.get(id=pk).delete()
        messages.warning(request, "Attendance Deleted!")
    except:
        messages.error(request, 'Error Occured')
    return redirect(request.META['HTTP_REFERER'])


def add_attendance(request, pk):
    student = MyUser.objects.get(id=pk)
    if request.method == "POST":
        try:
            if request.POST.get('attendance') == 'on':
                att = True
            else:
                att = False
            new_att = Attendance.objects.create(date=request.POST.get(
                'date'), student=MyUser.objects.get(id=pk), mark_attendance=att)
            new_att.save()
            messages.success(request, 'Attendance Saved!')
            return redirect(request.META['HTTP_REFERER'])
        except:
            messages.error(request, 'Eror!')
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'add_attendance.html', {'student': student})


def delete_student(request, pk):
    try:
        MyUser.objects.get(id=pk).delete()
        messages.warning(request, "Student Deleted!")
    except:
        messages.error(request, 'Error Occured')
    return redirect(request.META['HTTP_REFERER'])


def leave_approvel(request):
    all_leave = Leave.objects.all().order_by('-id')

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


def leave_approvel_response(request, pk, val):
    appr = Leave.objects.get(id=pk)
    if val == 1:
        appr.approve = True
        appr.save()
    else:
        appr.approve = False
        appr.save()
    return redirect(request.META['HTTP_REFERER'])


def report(request, pk):
    student = MyUser.objects.get(id=pk)
    total_leaves = Leave.objects.all().filter(student=student).count()
    total_present = Attendance.objects.all().filter(
        student=student, mark_attendance=True).count()
    total_absent = Attendance.objects.all().filter(
        student=student, mark_attendance=False).count()
    context = {'total_leaves': total_leaves,
               'total_present': total_present,
               'total_absent': total_absent,
               'student': student

               }
    return render(request, 'student_report.html', context)


def fetch_record(request):
    if request.method == "POST":
        from_date = timezone.datetime.strptime(
            request.POST.get('from_date'), "%Y-%m-%d").date()
        to_date = timezone.datetime.strptime(
            request.POST.get('to_date'), "%Y-%m-%d").date()
        Student = MyUser.objects.get(id=request.POST.get('stu'))
        data = Attendance.objects.filter(
            date__gte=from_date, date__lte=to_date, student=Student)
        total_present = Attendance.objects.filter(
            date__gte=from_date, date__lte=to_date, student=Student, mark_attendance=True).count()
        total_absent = Attendance.objects.filter(
            date__gte=from_date, date__lte=to_date, student=Student, mark_attendance=False).count()
        total_leaves = Leave.objects.filter(student=Student).count()
        return render(request, 'student_report.html', {
            'data': data,
            'student': Student,
            'total_present': total_present,
            'total_absent': total_absent,
            'total_leaves': total_leaves,

        })
    return redirect(reverse_lazy('fetch_record'))


def complete_report(request):
    if request.method == "POST":
        all_student = MyUser.objects.all().filter(user_type=1).count()
        from_date = timezone.datetime.strptime(
            request.POST.get('from_date'), "%Y-%m-%d").date()
        to_date = timezone.datetime.strptime(
            request.POST.get('to_date'), "%Y-%m-%d").date()
        data = Attendance.objects.filter(
            date__gte=from_date, date__lte=to_date)
        present = Attendance.objects.filter(
            date__gte=from_date, date__lte=to_date, mark_attendance=True).count()
        absent = Attendance.objects.filter(
            date__gte=from_date, date__lte=to_date, mark_attendance=False).count()
        total_leave = Leave.objects.filter(
            date__gte=from_date, date__lte=to_date).count()
        context = {
            'all_student': all_student,
            'present': present,
            'absent': absent,
            'total_leave': total_leave,
        }
        return render(request, 'complete_report.html', context)
    all_student = MyUser.objects.all().filter(user_type=1).count()
    present = Attendance.objects.all().filter(mark_attendance=True).count()
    absent = Attendance.objects.all().filter(mark_attendance=False).count()
    total_leave = Leave.objects.all().filter(approve=True).count()
    context = {
        'all_student': all_student,
        'present': present,
        'absent': absent,
        'total_leave': total_leave,
    }
    return render(request, 'complete_report.html', context)
