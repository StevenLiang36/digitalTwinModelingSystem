from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect
from UMS.models import UserInfo, MyTeam
from django import forms
from UMS import models

def index(request):
    return render(request, "index.html") # 整合主页

def leftSidebar(request):
    return render(request,"left-sidebar.html")

def rightSidebar(request):
    return render(request,"right-sidebar.html")

def noSidebar(request):
    return render(request,"no-sidebar.html")

def signUp(request):
    return render(request,"signUp.html")

def accountCreated(request):
    return render(request, "accountCreated.html")

class LoginForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        widget=forms.TextInput(attrs={"class": "form-control",'autocomplete': 'off'}),
        required=True
    )
    password = forms.CharField(
        label='密码',
        widget=forms.PasswordInput(attrs={"class": "form-control",'autocomplete': 'off'}),
        required=True
    )

def login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # user = models.UserInfo.objects.filter(username=username).first()
        user = models.UserInfo.objects.filter(username=username).first()

        if user and password == user.password:
            # 密码正确：
            request.session["userInfo"] = {'id': user.id, 'name': user.username} # cookie
            return redirect('/index/')
        else:
            # 密码错误：
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {'form': form})

    return render(request, 'login.html', {'form': form})

def adminLogin(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'adminLogin.html', {'form': form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # user = models.UserInfo.objects.filter(username=username).first()
        user = models.Admin.objects.filter(username=username).first()

        if user and password == user.password:
            # 密码正确：
            request.session["userInfo"] = {'id': user.id, 'name': user.username} # cookie
            return redirect('/userList/')
        else:
            # 密码错误：
            form.add_error("password", "用户名或密码错误")
            return render(request, 'adminLogin.html', {'form': form})

    return render(request, 'adminLogin.html', {'form': form})

def userAdd(request):
    if request.method == "GET":
        form = LoginForm
        return render(request, 'signUp.html')

    form = LoginForm(data=request.POST)
    if form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data['password']

        if username != None and password != None:
            UserInfo.objects.create(username=username, password=password)
            return redirect("/accountCreated/")
        else:
            form.add_error("password", "用户名或密码不能为空")
            return render(request, 'signUp.html', {'form': form})

    return render(request, 'signUp.html', {'form': form})