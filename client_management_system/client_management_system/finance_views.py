from django.shortcuts import render,redirect
from taggapp.models import Finance,Sales, HR, Support, CustomUser, Leads, Send_Fin_Notification,Send_Support_Notification,\
    Send_Sale_Notification,Send_Hr_Notification,Direct,Local_Direct,SID, Finance_leave
from django.contrib import messages

def HOME(request):

    return render(request, 'finance/home.html')


def FIN_RECEIVE_NOTIFICATION(request):
    finance = Finance.objects.filter(admin=request.user.id)
    for i in finance:
        finance_id = i.id
        see_fin_notification = Send_Fin_Notification.objects.filter(finance_id=finance_id)
        context = {
            'see_fin_notification': see_fin_notification
        }
        return render(request, 'finance/fin_receive_notification.html', context)


def CREDIT_NOTIFICATION(request):
    support = Support.objects.all()
    finsee_notification = Send_Support_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'support': support,
        'finsee_notification': finsee_notification,
    }
    return render(request, 'finance/credit_notification.html', context)


def FIN_SAVE_NOTIFICATION(request):

    if request.method == "POST":
        support_id = request.POST.get('support_id')
        message = request.POST.get('message')

        support = Support.objects.get(admin=support_id)
        notification = Send_Support_Notification(
            support_id=support,
            message=message,
        )
        notification.save()
        messages.success(request, 'Notification Successfully Sent!')
        return redirect('credit_notification')


def FIN_MARK_AS_DONE(request,status):
    notification = Send_Fin_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('fin_receive_notification')


def ADD_DIRECT_ROUTE(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        operator = request.POST.get('operator')
        rates = request.POST.get('rates')
        required = request.POST.get('required')
        documents = request.POST.get('documents')
        tat = request.POST.get('tat')
        features = request.POST.get('features')

        emp = Direct(
            country=country,
            operator=operator,
            rates=rates,
            required=required,
            documents=documents,
            tat=tat,
            features=features,
        )
        emp.save()
        messages.success(request, "Lead Added Successfully")
        return redirect('add_direct')

    context = {
    }
    return render(request, 'finance/add_direct.html', context)


def VIEW_DIRECT(request):
    view = Direct.objects.all()
    context = {
        'view': view,
    }
    return render(request, 'finance/view_direct.html', context)

def EDIT_DIRECT(request, id):
    direct = Direct.objects.filter(id = id)

    context = {
        'direct':direct,
    }
    return render(request, 'finance/edit_direct.html', context)

def DELETE_DIRECT(request, id):
    direct = Direct.objects.get(id=id)
    direct.delete()
    messages.success(request, 'Record Are Successfully Deleted!')
    return redirect('view_direct')


def UPDATE_DIRECT(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        country = request.POST.get('country')
        operator = request.POST.get('operator')
        rates = request.POST.get('rates')
        required = request.POST.get('required')
        documents = request.POST.get('documents')
        tat = request.POST.get('tat')
        features = request.POST.get('features')

        emp = Direct(
            id=id,
            country=country,
            operator=operator,
            rates=rates,
            required=required,
            documents=documents,
            tat=tat,
            features=features,
        )
        emp.save()
        messages.success(request, "Route Updated Successfully")
        return redirect('view_direct')
    return render(request, 'finance/edit_direct.html')


def ADD_LOCAL_DIRECT_ROUTE(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        operator = request.POST.get('operator')
        rates = request.POST.get('rates')
        required = request.POST.get('required')
        documents = request.POST.get('documents')
        tat = request.POST.get('tat')
        features = request.POST.get('features')

        emp = Local_Direct(
            country=country,
            operator=operator,
            rates=rates,
            required=required,
            documents=documents,
            tat=tat,
            features=features,
        )
        emp.save()
        messages.success(request, "Route Added Successfully")
        return redirect('add_local_direct')

    context = {
    }
    return render(request, 'finance/add_local_direct.html', context)


def VIEW_LOCAL_DIRECT(request):
    view = Local_Direct.objects.all()
    context = {
        'view': view,
    }
    return render(request, 'finance/view_local_direct.html', context)


def EDIT_LOCAL_DIRECT(request, id):
    local_direct = Local_Direct.objects.filter(id = id)

    context = {
        'local_direct':local_direct,
    }
    return render(request, 'finance/edit_local_direct.html', context)


def DELETE_LOCAL_DIRECT(request, id):
    local_direct = Local_Direct.objects.get(id=id)
    local_direct.delete()
    messages.success(request, 'Record Are Successfully Deleted!')
    return redirect('view_local_direct')


def UPDATE_LOCAL_DIRECT(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        country = request.POST.get('country')
        operator = request.POST.get('operator')
        rates = request.POST.get('rates')
        required = request.POST.get('required')
        documents = request.POST.get('documents')
        tat = request.POST.get('tat')
        features = request.POST.get('features')

        emp = Local_Direct(
            id=id,
            country=country,
            operator=operator,
            rates=rates,
            required=required,
            documents=documents,
            tat=tat,
            features=features,
        )
        emp.save()
        messages.success(request, "Route Updated Successfully")
        return redirect('view_local_direct')
    return render(request, 'finance/edit_local_direct.html')


def ADD_SID_ROUTE(request):
    if request.method == 'POST':
        country = request.POST.get('country')
        operator = request.POST.get('operator')
        rates = request.POST.get('rates')
        required = request.POST.get('required')
        documents = request.POST.get('documents')
        tat = request.POST.get('tat')
        features = request.POST.get('features')

        emp = SID(
            country=country,
            operator=operator,
            rates=rates,
            required=required,
            documents=documents,
            tat=tat,
            features=features,
        )
        emp.save()
        messages.success(request, "Lead Added Successfully")
        return redirect('add_sid')

    context = {
    }
    return render(request, 'finance/add_sid.html', context)


def VIEW_SID(request):
    view = SID.objects.all()
    context = {
        'view': view,
    }
    return render(request, 'finance/view_sid.html', context)


def EDIT_SID(request, id):
    sid = SID.objects.filter(id = id)

    context = {
        'sid':sid,
    }
    return render(request, 'finance/edit_sid.html', context)


def DELETE_SID(request, id):
    sid = SID.objects.get(id=id)
    sid.delete()
    messages.success(request, 'Record Are Successfully Deleted!')
    return redirect('view_sid')


def UPDATE_SID(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        country = request.POST.get('country')
        operator = request.POST.get('operator')
        rates = request.POST.get('rates')
        required = request.POST.get('required')
        documents = request.POST.get('documents')
        tat = request.POST.get('tat')
        features = request.POST.get('features')

        emp = SID(
            id=id,
            country=country,
            operator=operator,
            rates=rates,
            required=required,
            documents=documents,
            tat=tat,
            features=features,
        )
        emp.save()
        messages.success(request, "Route Updated Successfully")
        return redirect('view_sid')
    return render(request, 'finance/edit_sid.html')

def FINANCE_APPLY_LEAVE(request):
    finance = Finance.objects.filter(admin = request.user.id)
    for i in finance:
        finance_id = i.id
        finance_leave_history = Finance_leave.objects.filter(finance_id = finance_id)
        context = {
            'finance_leave_history':finance_leave_history,
        }
        return render(request, 'finance/finance_apply_leave.html', context)

def FINANCE_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_reason = request.POST.get('leave_reason')

        finance = Finance.objects.get(admin = request.user.id)

        leave = Finance_leave(
            finance_id = finance,
            date = leave_date,
            reason = leave_reason,
        )

        leave.save()
        messages.success(request, "Leave Successfully Applied!")
        return redirect('finance_apply_leave')


def ON_BOARD_REQUEST(request):
    client = Leads.objects.filter(status=1)

    context = {
        'client':client
    }
    return render(request, 'finance/on_board_req.html', context)


def CLIENT_BOARD(request,id):
   board = Leads.objects.get(id=id)
   board.on_board = 1
   board.save()
   return redirect('on_board_req')


def CLIENT_NOT_BOARD(request, id):
    not_board = Leads.objects.get(id=id)
    not_board.on_board = 2
    not_board.save()
    return redirect('on_board_req')