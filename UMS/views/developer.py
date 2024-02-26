from UMS.models import UserInfo, MyTeam
from django.shortcuts import render, HttpResponse, redirect

# from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login/')
def developerList(request):
    data_list = MyTeam.objects.all()
    return render(request, 'developerList.html', {'data_list': data_list})