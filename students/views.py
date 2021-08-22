from django.shortcuts import render
from django.http import JsonResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
from students.models import Attendance
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


