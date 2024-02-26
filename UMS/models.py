from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length = 32)
    password = models.CharField(verbose_name='密码',max_length = 64)

    # authority_choices = (
    #     (1, "管理员"),
    #     (2, "用户")
    # )
    # authority = models.SmallIntegerField(verbose_name="权限", choices=authority_choices, default=2)

class MyTeam(models.Model):
    name = models.CharField(verbose_name='成员名',max_length = 32)
    email = models.CharField(verbose_name='邮箱联系方式', max_length=64)

# try
class Admin(models.Model):
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)