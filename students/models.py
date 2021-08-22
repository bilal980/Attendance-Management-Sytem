from django.db import models
from account.models import MyUser
# Create your models here.

class Attendance(models.Model):

    student=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    mark_attendance=models.BooleanField(default=False)
    date=models.DateTimeField(default=None)
    def __str__(self):
        return self.student.email
