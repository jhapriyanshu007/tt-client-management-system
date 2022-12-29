from django.db import models

from django.contrib.auth.models import AbstractUser


# Create your models here.
class CustomUser(AbstractUser):
    USER = (
        (1, 'HOD'),
        (2, 'FINANCE'),
        (3, 'SALES'),
        (4, 'HR'),
        (5, 'SUPPORT')

    )
    user_type = models.CharField(choices= USER,max_length=50,default=1)


# class Employe_Id(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Finance(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    father_mob = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    permanent_add = models.TextField(max_length=100)
    username = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class Sales(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    father_mob = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    permanent_add = models.TextField(max_length=100)
    username = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class HR(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    father_mob = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    permanent_add = models.TextField(max_length=100)
    username = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name

class Support(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    employee_id = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    dob = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    joining_date = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    father_mob = models.CharField(max_length=100)
    father_occupation = models.CharField(max_length=100)
    mother_name = models.CharField(max_length=100)
    mother_occupation = models.CharField(max_length=100)
    permanent_add = models.TextField(max_length=100)
    username = models.TextField(max_length=100)
    password = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name


class Leads(models.Model):
    # admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    contact_person = models.CharField(max_length=100,null=True)
    company_name = models.CharField(max_length=100,null=True)
    email_id = models.CharField(max_length=100,null=True)
    contact_number = models.CharField(max_length=100,null=True)
    product = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    lead_source = models.CharField(max_length=100,null=True)
    date = models.CharField(max_length=100,null=True)
    address = models.CharField(max_length=100,null=True)
    feedback = models.CharField(max_length=100,null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name


class Send_Fin_Notification(models.Model):
    finance_id = models.ForeignKey(Finance,on_delete=models.CASCADE, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.finance_id.admin.first_name


class Send_Support_Notification(models.Model):
    support_id = models.ForeignKey(Support,on_delete=models.CASCADE, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.support_id.admin.first_name


class Send_Sale_Notification(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.sale_id.admin.first_name


class Send_Hr_Notification(models.Model):
    hr_id = models.ForeignKey(HR,on_delete=models.CASCADE, null=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.hr_id.admin.first_name

class Direct(models.Model):
    country = models.CharField(max_length=100, null=True)
    operator = models.CharField(max_length=100, null=True)
    rates = models.CharField(max_length=100, null=True)
    required = models.CharField(max_length=100, null=True)
    documents = models.CharField(max_length=100, null=True)
    tat = models.CharField(max_length=100, null=True)
    features = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.country)

class Local_Direct(models.Model):
    country = models.CharField(max_length=100, null=True)
    operator = models.CharField(max_length=100, null=True)
    rates = models.CharField(max_length=100, null=True)
    required = models.CharField(max_length=100, null=True)
    documents = models.CharField(max_length=100, null=True)
    tat = models.CharField(max_length=100, null=True)
    features = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.country)

class SID(models.Model):
    country = models.CharField(max_length=100, null=True)
    operator = models.CharField(max_length=100, null=True)
    rates = models.CharField(max_length=100, null=True)
    required = models.CharField(max_length=100, null=True)
    documents = models.CharField(max_length=100, null=True)
    tat = models.CharField(max_length=100, null=True)
    features = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.country)

class Sales_leave(models.Model):
    sale_id = models.ForeignKey(Sales, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    reason = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sale_id.admin.first_name

class Finance_leave(models.Model):
    finance_id = models.ForeignKey(Finance, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    reason = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.finance_id.admin.first_name

class Support_leave(models.Model):
    support_id = models.ForeignKey(Support, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    reason = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.support_id.admin.first_name

class HR_leave(models.Model):
    hr_id = models.ForeignKey(HR, on_delete=models.CASCADE)
    date = models.CharField(max_length=100)
    reason = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hr_id.admin.first_name