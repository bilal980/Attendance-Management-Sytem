from account.models import MyUser
from django.shortcuts import redirect, render
from django.http import JsonResponse
from django.utils import timezone
from django.urls import reverse_lazy
from django.contrib import messages
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt
from students.models import Attendance, Leave
# Create your views here.
def student_home(request):
    return render(request,'student_home.html')

@csrf_exempt
def attendace(request):
    if request.method =="POST":
        att=False
        if request.POST.get('attendance') == 'true':
            att=True
        save_att = Attendance.objects.create(
            student=request.user, mark_attendance=att, date=timezone.datetime.today().date()).save()
        return JsonResponse({'msg':'done'})

def check_attendace(request):
    date = timezone.datetime.today().date()
    if Attendance.objects.filter(student=request.user,date=date).exists():
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
        
    att=Attendance.objects.all().filter(student=request.user)
    p=Paginator(att,6)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        page_obj = p.page(1)
    except EmptyPage:
        # if page is empty then return last page
        page_obj = p.page(p.num_pages)
    context={'page_obj':page_obj,}

    return render(request,'attendance_table.html',context)

def update_profile(request):
    if request.method == 'POST':
        try:
            user = MyUser.objects.get(email=request.user)
            if request.POST.get('email') is not None:
                user.email = request.POST.get('email')
                user.save()
            
            if request.FILES:
                img = request.FILES['picture']
                user.picture = img
                user.save()
            messages.success(request, 'Updated Successfully!')
            return redirect(request.META['HTTP_REFERER'])
        except:
            messages.error(request, 'Some Error Occured!')
            return redirect(request.META['HTTP_REFERER'])
    return render(request, 'update_profile.html')

def leave_table(request):
    user = request.user
    leaves = Leave.objects.all().filter(student=user).order_by('-id')
    p = Paginator(leaves,7)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)  
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)
        
    context = {'page_obj': page_obj, }
    
    return render(request, 'leave_table.html',context)
