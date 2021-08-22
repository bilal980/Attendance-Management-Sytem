from django.db import models
from account.models import MyUser
# Create your models here.

class Attendance(models.Model):

    student=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    mark_attendance=models.BooleanField(default=False)
    date=models.DateTimeField(default=None)
    def __str__(self):
        return self.student.email

class Leave(models.Model):
    date=models.DateField()
    reason=models.TextField(max_length=300,blank=True,null=True)
    student=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    approve=models.BooleanField(default=False)
    
    def __str__(self):
        return self.student.email
    