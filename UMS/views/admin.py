from django.shortcuts import render
from UMS import models

from django.core.paginator import Paginator
# from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login/')
def adminList(request):

    data_dict = {}

    search_data = request.GET.get('srh', "")

    # 分页
    page = int(request.GET.get('page',1))
    page_size = 10

    if search_data:
        data_dict["username__contains"] = search_data
        data_list = models.Admin.objects.filter(**data_dict).order_by()
    else:
        data_list = models.Admin.objects.all()

    paginator = Paginator(data_list, page_size)
    data_list = paginator.get_page(page)

    context = {
        'data_list': data_list,
        'search_data': search_data
    }

    return render(request, 'adminList.html', context)