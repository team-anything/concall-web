from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee
from issues.models import Iss
from django.contrib.auth.decorators import login_required

@login_required(login_url="/Accounts/login")
def home(request):
    Employees = Employee.objects.all();
    employ=request.user.username
    print("XXXXXXXXXXXXXXXXX",employ)
    emps = Employee.objects.get(name=employ)
    iss=Iss.objects.all()
    string='/Empinf/'+emps.slug
    print("XXXXXXXXXXXXXXXXXXXX", string)
    return redirect(string)

def emp_detail(request, slug):
    #return HttpResponse(slug)
    emps = Employee.objects.get(slug=slug)
    iss=Iss.objects.all().order_by("-priority")
    return render(request, 'Empinf/issues.html', { 'emps': emps,'Iss':iss })
#
# @login_required(login_url="/accounts/login/")
# def article_create(request):
#     return render(request, 'articles/article_create.html')

def record(request):
    employee=request.user.username
    emp=Employee.objects.get(name=employee)
    pending=emp.issues_pending
    resolved=emp.total_issues
    return render(request, 'Empinf/record.html', {'pen':pending, 'res':resolved})
