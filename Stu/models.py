from django.db import models

# Create your models here.
class StuInfo(models.Model):

    stunum = models.CharField('学号', primary_key=True,null=False,unique=True,max_length=20)
    stuname = models.CharField('姓名', max_length=20)
    stuphone = models.CharField('联系方式',max_length=15)
    stubirth = models.DateField('出生日期', max_length=20)
    stusex = models.IntegerField('性别',choices=((1,'男'),(0,'女')))
    stuidcard = models.CharField('身份证',max_length=20)
    stumajor = models.CharField('专业',max_length=50)
    stufaculty = models.CharField('学院',max_length=50)
    stuimg = models.CharField('照片',max_length=200,null=True)
    stuin = models.DateField('入学年份',max_length=20)
    stuadress = models.CharField('住址',max_length=200,null=True)

    class Meta:
        db_table='stuinfo'
        ordering = ('stunum',)

