"""client_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views, hod_views, support_views, sales_views, hr_views, finance_views

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('base/', views.BASE, name='base'),
                  path('', views.LOGIN, name='login'),
                  path('dologout', views.DOLOGOUT, name='logout'),
                  path('dologin', views.dologin, name='dologin'),
                  path('profile', views.PROFILE, name='profile'),
                  path('profile/update', views.PROFILE_UPDATE, name='profile_update'),
                  path('hod/home', hod_views.HOME, name='hod_home'),

                  path('hod/add/fin', hod_views.Add_FIN, name='add_fin'),
                  path('hod/add/sale', hod_views.Add_SALE, name='add_sale'),
                  path('hod/add/hr', hod_views.Add_HR, name='add_hr'),
                  path('hod/add/support', hod_views.Add_SUPPORT, name='add_support'),

                  path('hod/view/fin', hod_views.VIEW_FIN, name='view_fin'),
                  path('hod/view/sale', hod_views.VIEW_SALES, name='view_sale'),
                  path('hod/view/hr', hod_views.VIEW_HR, name='view_hr'),
                  path('hod/view/support', hod_views.VIEW_SUPPORT, name='view_support'),

                  path('hod/edit/fin/<str:id>', hod_views.EDIT_FIN, name='edit_fin'),
                  path('hod/edit/sale/<str:id>', hod_views.EDIT_SALES, name='edit_sale'),
                  path('hod/edit/hr/<str:id>', hod_views.EDIT_HR, name='edit_hr'),
                  path('hod/edit/support/<str:id>', hod_views.EDIT_SUPPORT, name='edit_support'),

                  path('hod/delete/fin/<str:admin>', hod_views.DELETE_FIN, name='delete_fin'),
                  path('hod/delete/hr/<str:admin>', hod_views.DELETE_HR, name='delete_hr'),
                  path('hod/delete/sale/<str:admin>', hod_views.DELETE_SALE, name='delete_sale'),
                  path('hod/delete/support/<str:admin>', hod_views.DELETE_SUPPORT, name='delete_support'),

                  path('hod/update/fin', hod_views.UPDATE_FIN, name='update_fin'),
                  path('hod/update/sale', hod_views.UPDATE_SALES, name='update_sale'),
                  path('hod/update/hr', hod_views.UPDATE_HR, name='update_hr'),
                  path('hod/update/support', hod_views.UPDATE_SUPPORT, name='update_support'),

                  path('hod/add/lead', hod_views.ADD_LEAD, name='add_lead'),
                  path('hod/view_lead', hod_views.VIEW_LEAD, name='view_lead'),
                  path('hod/edit/lead/<str:id>', hod_views.EDIT_LEAD, name='edit_lead'),
                  path('hod/update/lead', hod_views.UPDATE_LEAD, name='update_lead'),
                  path('hod/delete/lead/<str:id>', hod_views.DELETE_LEAD, name='delete_lead'),

                  path('hod/send_notification', hod_views.SEND_NOTIFICATION, name='send_notification'),
                  path('hod/save_notification', hod_views.SAVE_NOTIFICATION, name='save_notification'),

                  path('hod/sale_leave_view', hod_views.SALE_LEAVE_VIEW, name='sale_leave_view'),
                  path('hod/sale_approve_leave/<str:id>', hod_views.SALE_APPROVE_LEAVE, name='sale_approve_leave'),
                  path('hod/sale_disapprove_leave/<str:id>', hod_views.SALE_DISAPPROVE_LEAVE, name='sale_disapprove_leave'),

                  path('hod/support_leave_view', hod_views.SUPPORT_LEAVE_VIEW, name='support_leave_view'),
                  path('hod/support_approve_leave/<str:id>', hod_views.SUPPORT_APPROVE_LEAVE, name='support_approve_leave'),
                  path('hod/support_disapprove_leave/<str:id>', hod_views.SUPPORT_DISAPPROVE_LEAVE, name='support_disapprove_leave'),

                  # This is fin url
                  path('fin/home', finance_views.HOME, name='fin_home'),

                  path('fin/add_direct', finance_views.ADD_DIRECT_ROUTE, name='add_direct' ),
                  path('fin/view_direct', finance_views.VIEW_DIRECT, name='view_direct'),
                  path('fin/edit_direct/<str:id>', finance_views.EDIT_DIRECT, name='edit_direct' ),
                  path('fin/update_direct', finance_views.UPDATE_DIRECT, name='update_direct'),
                  path('fin/delete_direct/<str:id>', finance_views.DELETE_DIRECT, name='delete_direct'),

                  path('fin/add_local_direct', finance_views.ADD_LOCAL_DIRECT_ROUTE, name='add_local_direct' ),
                  path('fin/view_local_direct', finance_views.VIEW_LOCAL_DIRECT, name='view_local_direct'),
                  path('fin/edit_local_direct/<str:id>', finance_views.EDIT_LOCAL_DIRECT, name='edit_local_direct'),
                  path('fin/update_local_direct', finance_views.UPDATE_LOCAL_DIRECT, name='update_local_direct'),
                  path('fin/delete_local_direct/<str:id>', finance_views.DELETE_LOCAL_DIRECT, name='delete_local_direct'),

                  path('fin/add_sid', finance_views.ADD_SID_ROUTE, name='add_sid'),
                  path('fin/view_sid', finance_views.VIEW_SID, name='view_sid'),
                  path('fin/edit_sid/<str:id>', finance_views.EDIT_SID, name='edit_sid'),
                  path('fin/update_sid', finance_views.UPDATE_SID, name='update_sid'),
                  path('fin/delete_sid/<str:id>', finance_views.DELETE_SID, name='delete_sid'),

                  path('fin/fin_receive_notification', finance_views.FIN_RECEIVE_NOTIFICATION, name='fin_receive_notification'),
                  path('fin/fin_mark_as_done/<str:status>', finance_views.FIN_MARK_AS_DONE, name='fin_mark_as_done'),
                  path('fin/credit_notification', finance_views.CREDIT_NOTIFICATION, name='credit_notification'),
                  path('fin/fin_save_notification', finance_views.FIN_SAVE_NOTIFICATION, name='fin_save_notification'),

                  # This is Sale url

                  path('sale/home', sales_views.HOME, name='sale_home'),
                  # path('sale/notification', sales_views.NOTIFICATION, name='notification'),
                  path('sale/view_leads', sales_views.VIEW_LEADS, name='view_leads'),
                  path('sale/edit_leads/<str:id>', sales_views.EDIT_LEADS, name='edit_leads'),
                  path('sale/update_lead', sales_views.UPDATE_LEAD, name='update_lead'),
                  path('sale/cred_notification', sales_views.CRED_NOTIFICATION, name='cred_notification'),
                  path('sale/sale_receive_notification', sales_views.SALE_RECEIVE_NOTIFICATION, name='sale_receive_notification'),
                  path('sale/sale_save_notification', sales_views.SALE_SAVE_NOTIFICATION, name='sale_save_notification'),
                  path('sale/sale_mark_as_done/<str:status>', sales_views.SALE_MARK_AS_DONE, name='sale_mark_as_done'),
                  path('sale/apply_leave', sales_views.SALE_APPLY_LEAVE, name='sale_apply_leave'),
                  path('sale/apply_leave_save_sale', sales_views.SALE_LEAVE_SAVE, name='sale_leave_save'),

                  # This is support url
                  path('support/home', support_views.HOME, name='support_home'),
                  path('support/su_receive_notification', support_views.RECEIVE_NOTIFICATION, name='su_receive_notification'),
                  path('support/su_cred_notification', support_views.SU_CRED_NOTIFICATION, name='su_cred_notification'),
                  path('support/support_save_notification', support_views.SUPPORT_SAVE_NOTIFICATION, name='support_save_notification'),
                  path('support/mark_su_done/<str:status>', support_views.SUPPORT_MARK_AS_DONE, name='mark_su_done'),
                  path('support/support_apply_leave', support_views.SUPPORT_APPLY_LEAVE, name='support_apply_leave'),
                  path('support/apply_leave_save_support', support_views.SUPPORT_LEAVE_SAVE, name='support_leave_save'),



              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
