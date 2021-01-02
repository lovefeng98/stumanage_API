from django.db import models

# Create your models here.
class User(models.Model):

    user_id = models.AutoField('用户ID',primary_key = True)
    username = models.CharField('用户名',unique=True,max_length=20)
    password = models.CharField('密码',unique=True,max_length=300)
    token = models.CharField('token',max_length=300,default='NULL')
    realname = models.CharField('真实姓名',max_length=20,default='NULL')
    status = models.BooleanField('状态',default=True)
    regtime = models.DateTimeField('注册时间',auto_now_add=True)

    class Meta:
        db_table='User'
        ordering = ('user_id',)