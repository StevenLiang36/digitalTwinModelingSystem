"""
URL configuration for digitalTwinModelingSystem project.

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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from UMS.views import user, developer, admin_view
from systemWeb import views
from Pre import views as pv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('', views.index),
    path('left-sidebar/', views.leftSidebar),
    path('right-sidebar/', views.rightSidebar),
    path('no-sidebar/', views.noSidebar),
    path('login/', views.login_view, name='login'),
    path('signUp/', views.userAdd, name='signUp'),
    path('logout/', views.logout_view, name='logout'),
    path('accountCreated/', views.accountCreated),

    # User Management System
    path('userList/', user.userInfoList),
    path('userInfo/<int:nid>/edit/', user.userEdit),
    path('userInfoDelete/', user.userDel),
    path('userListAdd/', user.userListAdd),

    path('adminLogin/', views.adminLogin),

    path('developerList/', developer.developerList),
    path('adminList/', admin_view.adminList),

    # Project Management
    path('projectList/', pv.project_list, name='project_list'),
    path('project/<int:pid>/', pv.project_detail, name='project_detail'),
    path('projectAdd/', pv.add_project_and_images, name='add_project_and_images'),
    path('projectDelete/<int:pid>/', pv.project_delete, name='project_delete'),
    path('addProjectImages/<int:pid>/', pv.add_project_images, name='add_project_images'),
    path('deleteImage/<int:iid>/', pv.image_delete, name='delete_image'),

    # Model Management
    path('showModels/<int:pid>/', pv.show_model, name='show_model'),
    path('modelAdd/<int:pid>/', pv.model_add, name='model_add'),

    # Case
    path('case/', pv.case_list, name='case_list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
