from django.shortcuts import render,redirect
from taggapp.models import Finance,Sales, HR, Support, CustomUser, Leads, Send_Fin_Notification,\
    Send_Support_Notification,Send_Sale_Notification,Send_Hr_Notification,Sales_leave, Clients

from django.contrib import messages

def HOME(request):
    return render(request, 'sales/home.html')


# def NOTIFICATION(request):
#     fin = Finance.objects.filter(admin=request.user.id)
#     for i in fin:
#         fin_id = i.id
#         notification = Send_Notification.objects.filter(finance_id=fin_id)
#     sale = Sales.objects.filter(admin=request.user.id)
#     hr = HR.objects.filter(admin=request.user.id)
#     support = Support.objects.filter(admin=request.user.id)

    # return render(request, 'sales/notification.html')


def VIEW_LEADS(request):
    view = Leads.objects.all()
    context = {
        'view': view,
    }
    return render(request, 'sales/view_leads.html', context)


def EDIT_LEADS(request, id):
    leads = Leads.objects.filter(id=id)

    context = {
        'leads': leads,
    }
    return render(request, 'sales/edits_leads.html', context)


def UPDATE_SALE_LEAD(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        contact_person = request.POST.get('contact_person')
        company_name = request.POST.get('company_name')
        email_id = request.POST.get('email')
        contact_number = request.POST.get('number')
        product = request.POST.get('product')
        state = request.POST.get('state')
        source = request.POST.get('source')
        lead_type = request.POST.get('lead_type')
        date = request.POST.get('generation_date')
        address = request.POST.get('address')
        feedback = request.POST.get('feedback')
        sale_person = request.POST.get('sale_person')

        lead = Leads(
            id=id,
            contact_person=contact_person,
            company_name=company_name,
            email_id=email_id,
            contact_number=contact_number,
            product=product,
            state=state,
            source=source,
            lead_type=lead_type,
            date=date,
            address=address,
            feedback=feedback,
            sale_person=sale_person,
        )

        lead.save()
        messages.success(request, 'Record Are Successfully Updated')
        return redirect('view_leads')
    return render(request, 'hod/edits_leads.html')


def CRED_NOTIFICATION(request):
    fin = Finance.objects.all()
    see_notification = Send_Fin_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'fin': fin,
        'see_notification': see_notification,
    }
    return render(request, 'sales/cred_notification.html', context)


def SALE_SAVE_NOTIFICATION(request):

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
        return redirect('cred_notification')


def SALE_RECEIVE_NOTIFICATION(request):
    sale = Sales.objects.filter(admin=request.user.id)
    for i in sale:
        sale_id = i.id
        see_sale_notification = Send_Sale_Notification.objects.filter(sale_id=sale_id)
        context = {
            'see_sale_notification': see_sale_notification
        }
        return render(request, 'finance/fin_receive_notification.html', context)


def SALE_MARK_AS_DONE(request,status):
    notification = Send_Sale_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('sale_receive_notification')


def SALE_APPLY_LEAVE(request):
    sale = Sales.objects.filter(admin = request.user.id)
    for i in sale:
        sale_id = i.id
        sale_leave_history = Sales_leave.objects.filter(sale_id = sale_id)
        context = {
            'sale_leave_history':sale_leave_history,
        }
        return render(request, 'sales/sale_apply_leave.html', context)


def SALE_LEAVE_SAVE(request):
    if request.method == "POST":
        leave_date = request.POST.get('leave_date')
        leave_reason = request.POST.get('leave_reason')

        sales = Sales.objects.get(admin = request.user.id)

        leave = Sales_leave(
            sale_id = sales,
            date = leave_date,
            reason = leave_reason,
        )

        leave.save()
        messages.success(request, "Leave Successfully Applied!")
        return redirect('sale_apply_leave')


def ON_BOARD_CLIENT(request):
    view = Leads.objects.filter(status=1).values()
    context = {
        'view': view,
    }
    return render(request, 'sales/on_board_cli.html', context)


def ON_BOARD_SUCCESS(request,id):
    board = Leads.objects.get(id=id)
    board.status = 1
    board.save()
    return redirect('sale_leave_view')


def ON_BOARD_FAILED(request,id):
    board = Leads.objects.get(id=id)
    board.status = 2
    board.save()
    return redirect('sale_leave_view')