from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class UserModel(UserAdmin):
    list_display = ['username','user_type']


admin.site.register(CustomUser,UserModel)
admin.site.register(Finance)
admin.site.register(Sales)
admin.site.register(HR)
admin.site.register(Support)
admin.site.register(Leads)
admin.site.register(Send_Fin_Notification)
admin.site.register(Send_Sale_Notification)
admin.site.register(Send_Hr_Notification)
admin.site.register(Send_Support_Notification)
admin.site.register(Direct)
admin.site.register(Local_Direct)
admin.site.register(SID)
admin.site.register(Sales_leave)