from django.db import models
from django.contrib.auth.models import AbstractUser
from account.manager import CustomUserManager
# Create your models here.


class MyUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'student'),
        (2, 'admin'),
    )
    email = models.EmailField(verbose_name='Email', max_length=60, unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default='1')
    phone=models.IntegerField(blank=True,null=True)
    picture = models.ImageField(upload_to='static/image/profile_pic/', null=True,blank=True)
    USERNAME_FIELD = 'email'
    username=None
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
