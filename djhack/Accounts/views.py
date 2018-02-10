from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from Empinf.models import Employee



def signup_view(request):
    if request.method == 'POST':
         form = UserCreationForm(request.POST)
         #return HttpResponse("chdb")
         if form.is_valid():
             user = form.save()
             #return HttpResponse(user)
             return redirect(request,'Empinf:home')
    else:
        form = UserCreationForm()
    return render(request, 'Accounts/signup.html', { 'form': form })

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # log the user in
            user = form.get_user()
            login(request, user)
            username= Employee.objects.get(name=user)
            slug=username.slug
            urlf="/Empinf/"+slug+"/"
            return redirect(urlf)
    else:
        form = AuthenticationForm()
    return render(request, 'Accounts/login.html', { 'form': form })

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('Empinf:home')
