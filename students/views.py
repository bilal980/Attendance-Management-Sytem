from django.shortcuts import redirect, render
from django.http import JsonResponse
import datetime
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from students.models import Attendance, Leave
# Create your views here.
def student_home(request):
    return render(request,'student_home.html')

@csrf_exempt
def attendace(request):
    if request.method =="POST":
        att = request.POST.get('attendance')
        if att=='true':
            att=True
        else:att=False
        save_att = Attendance.objects.create(student=request.user, mark_attendance=att,date=datetime.date.today())
        save_att.save()
        return JsonResponse({'msg':'done'})


def check_attendace(request):
    user=request.user   
    date=datetime.date.today()
    if Attendance.objects.filter(student=request.user,date=date).exists():
        print(Attendance.objects.get(student=user, date=date))
        return JsonResponse({
            'att':'True'
        })
    return JsonResponse({
        'att':'False'
    })


def leave(request):
    if request.method=="POST":
        reason=request.POST.get('reason')
        date=request.POST.get('date')
        new_leave=Leave.objects.create(date=date,reason=reason,student=request.user)
        new_leave.save()
        return redirect(reverse_lazy('student_home'))
    return render(request,'leave_form.html')


def attendance_table(request):
    user=request.user
    att=Attendance.objects.all()
    context={'attendace':att}
    return render(request,'attendance_table.html',context)