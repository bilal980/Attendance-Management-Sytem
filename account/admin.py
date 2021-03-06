from django.contrib import admin
from account.forms import MyUserChangeForm,MyUserCreationForm
from django.utils.translation import ugettext_lazy  as _
from account.models import MyUser
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = MyUser

    fieldsets = (
        (None, {'fields': ('email','first_name' ,'password', 'date_joined', 'picture',)}),

        (_('Permissions'), {
            'fields': ('is_active', 'user_type', 'is_staff', 'is_superuser', 'groups', 'user_permissions',),
        }),

    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'picture',),
        }),
    )
    list_display = ('email',)
    ordering = ('email',)


admin.site.register(MyUser, MyUserAdmin)
