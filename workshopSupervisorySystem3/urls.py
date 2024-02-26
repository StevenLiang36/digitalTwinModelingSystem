"""
URL configuration for workshopSupervisorySystem3 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from UMS.views import user,developer,admin
from systemWeb import views

urlpatterns = [
    # path('admin/', admin.site.urls),

    # System Web
    path('homePage/',views.toHomePageAndLogin),
    path('signUpPage/',views.userAdd),
    path('accCreated/',views.toAccCreatedPage),
    path('main/',views.toMainPage),
    path('contactUs/',views.teamInfoList),

    path('adminLogin/',views.adminLogin),

    path('index/',views.index), # 整合主页
    path('left-sidebar/',views.leftSidebar),
    path('right-sidebar/',views.rightSidebar),
    path('no-sidebar/',views.noSidebar),
    path('login/',views.login),


    # User Management System
    path('userList/',user.userInfoList),
    path('userInfo/<int:nid>/edit/',user.userEdit),
    path('userInfoDelete/',user.userDel),
    path('userListAdd/',user.userListAdd),

    path('developerList/',developer.developerList),
    path('adminList/',admin.adminList),

]
