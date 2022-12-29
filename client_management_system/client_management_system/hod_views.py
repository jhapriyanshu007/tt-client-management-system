from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from taggapp.models import Finance,Sales, HR, Support, CustomUser, Leads, Send_Fin_Notification,Send_Support_Notification,Send_Sale_Notification,Send_Hr_Notification
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    lead_count = Leads.objects.all().count()
    staff = CustomUser.objects.all().count()

    context = {
        'lead_count':lead_count,
        'staff': staff,
    }
    return render(request, 'hod/home.html', context)


@login_required(login_url='/')
def Add_FIN(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employeeId = request.POST.get('employeeId')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        joining_date = request.POST.get('joining_date')
        mobileNo = request.POST.get('mobileNo')
        email = request.POST.get('email')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        permanent_address = request.POST.get('permanent_address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Exist!')
            return redirect('add_fin')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is Already Exist!')
            return redirect('add_fin')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                user_type = 2
            )
            user.set_password(password)
            user.save()

            emp = Finance(
                admin = user,
                employee_id = employeeId,
                first_name = first_name,
                last_name = last_name,
                gender = gender,
                dob = dob,
                designation=designation,
                joining_date=joining_date,
                mobile = mobileNo,
                email = email,
                father_name = father_name,
                father_mob = father_mobile,
                father_occupation = father_occupation,
                mother_name = mother_name,
                mother_occupation =mother_occupation,
                permanent_add = permanent_address
            )
            emp.save()
            messages.success(request, "Employee Saves Successfully")
            return redirect('add_fin')

    context = {

    }
    return render(request, 'hod/add_fin.html', context)


@login_required(login_url='/')
def Add_SALE(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employeeId = request.POST.get('employeeId')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        joining_date = request.POST.get('joining_date')
        mobileNo = request.POST.get('mobileNo')
        email = request.POST.get('email')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        permanent_address = request.POST.get('permanent_address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Exist!')
            return redirect('add_sale')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is Already Exist!')
            return redirect('add_sale')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                user_type = 3
            )
            user.set_password(password)
            user.save()

            emp = Sales(
                admin=user,
                employee_id=employeeId,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                dob=dob,
                designation=designation,
                joining_date = joining_date,
                mobile=mobileNo,
                email=email,
                father_name=father_name,
                father_mob=father_mobile,
                father_occupation=father_occupation,
                mother_name=mother_name,
                mother_occupation=mother_occupation,
                permanent_add=permanent_address
            )
            emp.save()
            messages.success(request, "Employee Saves Successfully")
            return redirect('add_sale')

    context = {
    }
    return render(request, 'hod/add_sale.html', context)


@login_required(login_url='/')
def Add_HR(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employeeId = request.POST.get('employeeId')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        joining_date = request.POST.get('joining_date')
        mobileNo = request.POST.get('mobileNo')
        email = request.POST.get('email')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        permanent_address = request.POST.get('permanent_address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Exist!')
            return redirect('add_hr')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is Already Exist!')
            return redirect('add_hr')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                user_type = 4
            )
            user.set_password(password)
            user.save()

            emp = HR(
                admin=user,
                employee_id=employeeId,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                dob=dob,
                designation=designation,
                joining_date=joining_date,
                mobile=mobileNo,
                email=email,
                father_name=father_name,
                father_mob=father_mobile,
                father_occupation=father_occupation,
                mother_name=mother_name,
                mother_occupation=mother_occupation,
                permanent_add=permanent_address
            )
            emp.save()
            messages.success(request, "Employee Saves Successfully")
            return redirect('add_hr')

    context = {
    }
    return render(request, 'hod/add_hr.html', context)


@login_required(login_url='/')
def Add_SUPPORT(request):

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employeeId = request.POST.get('employeeId')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        joining_date = request.POST.get('joining_date')
        mobileNo = request.POST.get('mobileNo')
        email = request.POST.get('email')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        permanent_address = request.POST.get('permanent_address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request, 'Email is Already Exist!')
            return redirect('add_support')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request, 'Username is Already Exist!')
            return redirect('add_support')
        else:
            user = CustomUser(
                first_name = first_name,
                last_name = last_name,
                username = username,
                email = email,
                user_type = 5
            )
            user.set_password(password)
            user.save()

            emp = Support(
                admin=user,
                employee_id=employeeId,
                first_name=first_name,
                last_name=last_name,
                gender=gender,
                dob=dob,
                designation=designation,
                joining_date=joining_date,
                mobile=mobileNo,
                email=email,
                father_name=father_name,
                father_mob=father_mobile,
                father_occupation=father_occupation,
                mother_name=mother_name,
                mother_occupation=mother_occupation,
                permanent_add=permanent_address
            )
            emp.save()
            messages.success(request, "Employee Saves Successfully")
            return redirect('add_support')

    context = {

    }
    return render(request, 'hod/add_support.html', context)


def VIEW_FIN(request):
    view = Finance.objects.all()
    context = {
        'view': view,
    }
    return render(request, 'hod/view_fin.html', context)


def EDIT_FIN(request, id):
    fin = Finance.objects.filter(id = id)

    context = {
        'fin':fin,
    }
    return render(request, 'hod/edit_fin.html', context)


def UPDATE_FIN(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employeeId = request.POST.get('employeeId')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        joining_date = request.POST.get('joining_date')
        mobileNo = request.POST.get('mobileNo')
        email = request.POST.get('email')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        permanent_address = request.POST.get('permanent_address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        fin = Finance.objects.get(admin=id)
        fin.first_name = first_name
        fin.last_name = last_name
        fin.email = email
        fin.username = username
        fin.employee_id = employeeId
        fin.gender = gender
        fin.dob = dob
        fin.designation = designation
        fin.joining_date = joining_date
        fin.mobile = mobileNo
        fin.father_name = father_name
        fin.father_occupation = father_occupation
        fin.father_mob = father_mobile
        fin.mother_name = mother_name
        fin.mother_occupation = mother_occupation
        fin.permanent_add = permanent_address

        fin.save()
        messages.success(request, 'Record Are Successfully Updated')
        return redirect('view_fin')
    return render(request, 'hod/edit_fin.html')

def VIEW_SALES(request):
    view = Sales.objects.all()
    context = {
        'view': view,
    }
    return render(request, 'hod/view_sales.html', context)


def EDIT_SALES(request, id):
    sale = Sales.objects.filter(id = id)

    context = {
        'sale':sale,
    }
    return render(request, 'hod/edit_sales.html', context)


def UPDATE_SALES(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employeeId = request.POST.get('employeeId')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        joining_date = request.POST.get('joining_date')
        mobileNo = request.POST.get('mobileNo')
        email = request.POST.get('email')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        permanent_address = request.POST.get('permanent_address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        sale = Sales.objects.get(admin=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username
        sale.employee_id = employeeId
        sale.gender = gender
        sale.dob = dob
        sale.designation = designation
        sale.joining_date = joining_date
        sale.mobile = mobileNo
        sale.father_name = father_name
        sale.father_occupation = father_occupation
        sale.father_mob = father_mobile
        sale.mother_name = mother_name
        sale.mother_occupation = mother_occupation
        sale.permanent_add = permanent_address

        sale.save()
        messages.success(request, 'Record Are Successfully Updated')
        return redirect('view_sale')
    return render(request, 'hod/edit_sale.html')

def VIEW_HR(request):
    view = HR.objects.all()
    context = {
        'view': view,
    }
    return render(request, 'hod/view_hr.html', context)


def EDIT_HR(request, id):
    hr = HR.objects.filter(id = id)

    context = {
        'hr':hr,
    }
    return render(request, 'hod/edit_hr.html', context)


def UPDATE_HR(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employeeId = request.POST.get('employeeId')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        joining_date = request.POST.get('joining_date')
        mobileNo = request.POST.get('mobileNo')
        email = request.POST.get('email')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        permanent_address = request.POST.get('permanent_address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        hr = HR.objects.get(admin=id)
        hr.first_name = first_name
        hr.last_name = last_name
        hr.email = email
        hr.username = username
        hr.employee_id = employeeId
        hr.gender = gender
        hr.dob = dob
        hr.designation = designation
        hr.joining_date = joining_date
        hr.mobile = mobileNo
        hr.father_name = father_name
        hr.father_occupation = father_occupation
        hr.father_mob = father_mobile
        hr.mother_name = mother_name
        hr.mother_occupation = mother_occupation
        hr.permanent_add = permanent_address

        hr.save()
        messages.success(request, 'Record Are Successfully Updated')
        return redirect('view_hr')
    return render(request, 'hod/edit_hr.html')

def VIEW_SUPPORT(request):
    view = Support.objects.all()
    context = {
        'view': view,
    }
    return render(request, 'hod/view_support.html', context)


def EDIT_SUPPORT(request, id):
    support = Support.objects.filter(id = id)

    context = {
        'support':support,
    }
    return render(request, 'hod/edit_support.html', context)


def UPDATE_SUPPORT(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        employeeId = request.POST.get('employeeId')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        designation = request.POST.get('designation')
        joining_date = request.POST.get('joining_date')
        mobileNo = request.POST.get('mobileNo')
        email = request.POST.get('email')
        father_name = request.POST.get('father_name')
        father_occupation = request.POST.get('father_occupation')
        father_mobile = request.POST.get('father_mobile')
        mother_name = request.POST.get('mother_name')
        mother_occupation = request.POST.get('mother_occupation')
        permanent_address = request.POST.get('permanent_address')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = CustomUser.objects.get(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        user.save()

        support = Support.objects.get(admin=id)
        support.first_name = first_name
        support.last_name = last_name
        support.email = email
        support.username = username
        support.employee_id = employeeId
        support.gender = gender
        support.dob = dob
        support.designation = designation
        support.joining_date = joining_date
        support.mobile = mobileNo
        support.father_name = father_name
        support.father_occupation = father_occupation
        support.father_mob = father_mobile
        support.mother_name = mother_name
        support.mother_occupation = mother_occupation
        support.permanent_add = permanent_address

        support.save()
        messages.success(request, 'Record Are Successfully Updated')
        return redirect('view_support')
    return render(request, 'hod/edit_support.html')


def DELETE_FIN(request, admin):
    fin = CustomUser.objects.get(id=admin)
    fin.delete()
    messages.success(request, 'Record Are Successfully Deleted!')
    return redirect('view_fin')

def DELETE_HR(request, admin):
    hr = CustomUser.objects.get(id=admin)
    hr.delete()
    messages.success(request, 'Record Are Successfully Deleted!')
    return redirect('view_hr')

def DELETE_SALE(request, admin):
    sale = CustomUser.objects.get(id=admin)
    sale.delete()
    messages.success(request, 'Record Are Successfully Deleted!')
    return redirect('view_sale')

def DELETE_SUPPORT(request, admin):
    support = CustomUser.objects.get(id=admin)
    support.delete()
    messages.success(request, 'Record Are Successfully Deleted!')
    return redirect('view_support')


@login_required(login_url='/')
def ADD_LEAD(request):
    if request.method == "POST":
        contact_person = request.POST.get('contact_person')
        company_name = request.POST.get('company_name')
        email_id = request.POST.get('email')
        contact_number = request.POST.get('number')
        product = request.POST.get('product')
        state = request.POST.get('country-state')
        lead_source = request.POST.get('source')
        date = request.POST.get('generation_date')
        address = request.POST.get('address')
        feedback = request.POST.get('feedback')

        # if CustomUser.objects.filter(companyname=company_name).exists():
        #     messages.warning(request, 'This Company is Already Exist!')
        #     return redirect('add_lead')
        #
        # if CustomUser.objects.filter(contact=contact_number).exists():
        #     messages.warning(request, 'This Contact Number is Already Exist!')
        #     return redirect('add_lead')

        emp = Leads(
            contact_person=contact_person,
            company_name=company_name,
            email_id=email_id,
            contact_number=contact_number,
            product=product,
            state=state,
            lead_source=lead_source,
            date=date,
            address=address,
            feedback=feedback,
         )
        emp.save()
        messages.success(request, "Lead Added Successfully")
        return redirect('add_lead')

    context = {
    }
    return render(request, 'hod/add_lead.html', context)


def VIEW_LEAD(request):
    view = Leads.objects.all()
    context = {
        'view': view,
    }
    return render(request, 'hod/view_lead.html', context)


def EDIT_LEAD(request, id):
    lead = Leads.objects.filter(id=id)

    context = {
        'lead': lead,
    }
    return render(request, 'hod/edit_lead.html', context)


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
        return redirect('view_lead')
    return render(request, 'hod/edit_lead.html')


def DELETE_LEAD(request, id):
    lead = Leads.objects.get(id=id)
    lead.delete()
    messages.success(request, 'Record Are Successfully Deleted!')
    return redirect('view_lead')


def SEND_NOTIFICATION(request):
    fin = Finance.objects.all()
    sale = Sales.objects.all()
    hr = HR.objects.all()
    support = Support.objects.all()
    see_notification = Send_Notification.objects.all().order_by('-id')[0:5]
    context = {
        'fin': fin,
        'sale': sale,
        'hr': hr,
        'support': support,
        'see_notification': see_notification,
    }
    return render(request, 'hod/send_notification.html', context)


def SAVE_NOTIFICATION(request):

    if request.method == 'POST':
        message = request.POST.get('message')

        notification = Send_Notification(
            message = message,
        )
        notification.save()
        messages.success(request, 'Notification Successfully Sent!')
        return redirect('send_notification')


