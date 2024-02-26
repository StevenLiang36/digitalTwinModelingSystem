from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse, redirect

from UMS.models import UserInfo, MyTeam

from django import forms
from systemWeb.utils.encrypt import md5
from UMS import models


def toHomePageAndLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if UserInfo.objects.filter(username = username):
            if UserInfo.objects.filter(username = username)[0].password == password:
                return redirect('/main/')
            else:
                return HttpResponse('password incorrect')
        else:
            return HttpResponse('user not exist')
    return render(request, "homePage.html")

def userAdd(request):
    if request.method == "GET":
        return render(request,'signUpPage.html')
    #获取用户提交数据
    username = request.POST.get("username")
    password = request.POST.get("password")

    #添加到数据库
    UserInfo.objects.create(username=username, password=password)
    #添加后跳转到指定页面
    return redirect("/accCreated/")

def toAccCreatedPage(requeast):
    return render(requeast,"accCreated.html")

def toMainPage(request):
    return render(request,'mainPage.html')

def teamInfoList(request):
    data_list = MyTeam.objects.all()
    return render(request,'contactUs.html',{'data_list':data_list})

def toContactPage(request):
    return render(request, "contactUs.html")

# 廖子尧版本
def index(request):
    return render(request, "index.html") # 整合主页

def leftSidebar(request):
    return render(request,"left-sidebar.html")

def rightSidebar(request):
    return render(request,"right-sidebar.html")

def noSidebar(request):
    return render(request,"no-sidebar.html")

def login2(request):
    return render(request,"login2.html")

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

# try
# wpq版本
# class LoginForm(forms.Form):
#     username = forms.CharField(
#         label='用户名',
#         widget=forms.TextInput(attrs={"class":"form-control"}),
#         required=True
#     )
#     password = forms.CharField(
#         label='密码',
#         widget=forms.PasswordInput(attrs={"class":"form-control"}),
#         required=True
#     )
#
#     def clean_password(self):
#         password = self.cleaned_data.get("password")
#         return md5(password)
#
# def login(request):
#     if request.method == "GET":
#         form = LoginForm()
#         return render(request,'login.html',{'form': form})
#
#     form = LoginForm(data=request.POST)
#     if form.is_valid():
#         object = models.UserInfo.objects.filter(**form.cleaned_data).first()
#         # 密码错误：
#         if not object:
#             form.add_error("password","用户名或密码错误")
#             return render(request,'login.html',{'form':form})
#         # 密码正确：
#         return HttpResponse("提交成功")
#     return render(request, 'login.html', {'form': form})

# GPT版本
# from django.contrib.auth.hashers import make_password
# 添加用户时进行密码加密
# def userAdd(request):
#     if request.method == "GET":
#         return render(request, 'signUpPage.html')
#
#     # 获取用户提交数据
#     username = request.POST.get("username")
#     password = request.POST.get("password")
#
#     # 使用 make_password 处理密码
#     hashed_password = make_password(password)
#
#     # 添加到数据库
#     UserInfo.objects.create(username=username, password=hashed_password)
#
#     # 添加后跳转到指定页面
#     return redirect("/accCreated/")
#
# from django.contrib.auth.hashers import check_password
# 登陆时进行加密密码匹配
# class LoginForm(forms.Form):
#     username = forms.CharField(
#         label='用户名',
#         widget=forms.TextInput(attrs={"class": "form-control"}),
#         required=True
#     )
#     password = forms.CharField(
#         label='密码',
#         widget=forms.PasswordInput(attrs={"class": "form-control"}),
#         required=True
#     )
#
# def login(request):
#     if request.method == "GET":
#         form = LoginForm()
#         return render(request, 'login.html', {'form': form})
#
#     form = LoginForm(data=request.POST)
#     if form.is_valid():
#         username = form.cleaned_data['username']
#         password = form.cleaned_data['password']
#         print(username,password)
#         print(type(password))
#         user = models.UserInfo.objects.filter(username=username).first()
#         print(user)
#         print(user.password)
#         print(type(user.password))
#         if user:
#             print(True)
#         print(check_password(password, user.password))
#         pas = make_password(password)
#         print(pas)
#         print(check_password(password,pas))
#
#         if user and check_password(password, user.password):
#             # 密码正确：
#             return HttpResponse("提交成功")
#         else:
#             # 密码错误：
#             form.add_error("password", "用户名或密码错误")
#             return render(request, 'login.html', {'form': form})
#
#     return render(request, 'login.html', {'form': form})
