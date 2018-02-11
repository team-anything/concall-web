from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Employee
from issues.models import Iss
from django.contrib.auth.decorators import login_required

@login_required(login_url="/Accounts/login")
def home(request):
    Employees = Employee.objects.all();
    employ=request.user.username
    print(employ)
    emps = Employee.objects.get(name=employ)
    iss=Iss.objects.all()
    string='/Empinf/'+emps.slug
    return redirect(string)

def emp_detail(request, slug):
    #return HttpResponse(slug)
    emps = Employee.objects.get(slug=slug)
    iss=Iss.objects.all()
    return render(request, 'Empinf/issues.html', { 'emps': emps,'Iss':iss })
#
# @login_required(login_url="/accounts/login/")
# def article_create(request):
#     return render(request, 'articles/article_create.html')
