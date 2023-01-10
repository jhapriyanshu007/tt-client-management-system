from django.shortcuts import render,redirect
from taggapp.models import Finance,Sales, HR, Support, CustomUser, Leads, Send_Fin_Notification,Send_Support_Notification,Send_Sale_Notification,Send_Hr_Notification, Support_leave
from django.contrib import messages

def HOME(request):
    return render(request, 'support/home.html')


def SU_CRED_NOTIFICATION(request):
    fin = Finance.objects.all()
    see_notification = Send_Fin_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'fin': fin,
        'su_see_notification': see_notification,
    }
    return render(request, 'support/su_cred_notification.html', context)


def SUPPORT_SAVE_NOTIFICATION(request):
    if request.method == "POST":
        finance_id = request.POST.get('fin_id')
        message = request.POST.get('message')

        finance = Finance.objects.get(admin=finance_id)
        notification = Send_Fin_Notification(
            finance_id=finance,
            message=message,
        )
        notification.save()
        messages.success(request, 'Notification Successfully Sent!')
        return redirect('su_cred_notification')


def RECEIVE_NOTIFICATION(request):
    support = Support.objects.filter(admin=request.user.id)
    for i in support:
        support_id = i.id

        see_support_notification = Send_Support_Notification.objects.filter(support_id=support_id)

        context = {
            'see_support_notification': see_support_notification
        }
        return render(request, 'support/su_receive_notification.html', context)


def SUPPORT_MARK_AS_DONE(request,status):
    notification = Send_Support_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('su_receive_notification')

def SUPPORT_APPLY_LEAVE(request):
    support = Support.objects.filter(admin = request.user.id)
    for i in support:
        support_id = i.id
        support_leave_history = Support_leave.objects.filter(support_id = support_id)
        context = {
            'support_leave_history':support_leave_history,
        }
        return render(request, 'support/support_apply_leave.html', context)

def SUPPORT_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_reason = request.POST.get('leave_reason')

        support = Support.objects.get(admin = request.user.id)

        leave = Support_leave(
            support_id = support,
            date = leave_date,
            reason = leave_reason,
        )

        leave.save()
        messages.success(request, "Leave Successfully Applied!")
        return redirect('support_apply_leave')
