from django.shortcuts import render,redirect
from taggapp.models import Finance,Sales, HR, Support, CustomUser, Leads, Send_Fin_Notification,Send_Support_Notification,Send_Sale_Notification,Send_Hr_Notification
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
    return render(request, 'sales/edit_leads.html', context)


def UPDATE_LEAD(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        contact_person = request.POST.get('contact_person')
        company_name = request.POST.get('company_name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        product = request.POST.get('product')
        country_state = request.POST.get('country_state')
        source = request.POST.get('source')
        generation_date = request.POST.get('generation_date')
        address = request.POST.get('address')
        feedback = request.POST.get('feedback')

        lead = Leads(
            id=id,
            contact_person=contact_person,
            company_name=company_name,
            email_id=email,
            contact_number=number,
            product=product,
            state=country_state,
            lead_source=source,
            date=generation_date,
            address=address,
            feedback=feedback,
        )

        lead.save()
        messages.success(request, 'Record Are Successfully Updated')
        return redirect('view_leads')
    return render(request, 'hod/edit_leads.html')


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


def APPLY_LEAVE(request):
    return render(request, 'sales/apply_leave.html')