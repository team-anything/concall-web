from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import Iss
from Empinf.models import Employee
from django.contrib.auth.decorators import login_required


def issue_detail(request,issueid):
    # return HttpResponse(slug)
    iss = Iss.objects.get(issueid=issueid)
    return render(request, 'issues/issue_detail.html', { 'Iss': iss })
#
# @login_required(login_url="/accounts/login/")
# def article_create(request):
#     return render(request, 'articles/article_create.html')
#def add_issue():

#
def remove_issue(request,issueid):
     iss = Iss.objects.get(issueid=issueid)
     iss.resolve=True
     iss.save()
     empo=iss.agent
     empo.issues_pending=empo.issues_pending-1
     empo.save()
     s='/Empinf/'
     s+=str(empo.slug)
     return redirect(s)
