from django.contrib import admin
# from django.contrib.auth.models import User
from .models import Project, Image, ThreeDModel

# Register your models here.
admin.site.register(Project)
admin.site.register(Image)
admin.site.register(ThreeDModel)
