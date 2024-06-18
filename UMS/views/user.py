from UMS.models import UserInfo, MyTeam
from django.shortcuts import render, HttpResponse, redirect
from UMS import models

from django.core.paginator import Paginator


# from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login/')
def userInfoList(request):
    # data_list = UserInfo.objects.all()
    # return render(request, 'userList.html', {'data_list': data_list})

    data_dict = {}
    search_data = request.GET.get('srh', "")

    page = int(request.GET.get('page', 1))
    page_size = 10

    if search_data:
        data_dict["username__contains"] = search_data
        data_list = models.UserInfo.objects.filter(**data_dict).order_by()
    else:
        data_list = models.UserInfo.objects.all()

    paginator = Paginator(data_list, page_size)
    data_list = paginator.get_page(page)

    context = {
        'data_list': data_list,
        'search_data': search_data
    }

    return render(request, 'userList.html', context)


def userEdit(request, nid):
    if request.method == "GET":
        row_object = UserInfo.objects.filter(id=nid).first()
        return render(request, 'userListEdit.html', {"row_object": row_object})

    username = request.POST.get("username")
    password = request.POST.get("password")

    UserInfo.objects.filter(id=nid).update(username=username)
    UserInfo.objects.filter(id=nid).update(password=password)

    return redirect("/userList/")


def userDel(request):
    nid = request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/userList/")


# @login_required(login_url='/login/')
def userListAdd(request):
    if request.method == "GET":
        return render(request, 'userListAdd.html')
    # 获取用户提交数据
    username = request.POST.get("username")
    password = request.POST.get("password")
    # authority = request.POST.get("authority")

    # 添加到数据库
    UserInfo.objects.create(username=username, password=password)

    return redirect("/userList/")

# GPT版本
# from django.contrib.auth.hashers import make_password
#
# def userListAdd(request):
#     if request.method == "GET":
#         return render(request, 'userListAdd.html')
#     # 获取用户提交数据
#     username = request.POST.get("username")
#     password = request.POST.get("password")
#     # authority = request.POST.get("authority")
#     hashed_password = make_password(password)
#
#     # 添加到数据库
#     UserInfo.objects.create(username=username, password=hashed_password)
#
#     return redirect("/userList/")
