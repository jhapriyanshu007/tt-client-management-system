from django.shortcuts import render,redirect
from taggapp.models import Finance,Sales, HR, Support, CustomUser, Leads, Send_Fin_Notification,Send_Support_Notification,Send_Sale_Notification,Send_Hr_Notification
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