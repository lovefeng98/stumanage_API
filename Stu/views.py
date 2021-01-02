from time import strptime

from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from Stu.StuSerializer import AllStuinfoShowSerializer, AddStuinfoSerializer, EditStuinfoSerializer
from Stu.models import StuInfo
import random as r
#
# class AddIntosql():
#     first = ('张', '王', '李', '赵', '金', '艾', '单', '龚', '钱', '周', '吴', '郑', '孔', '曺', '严', '华', '吕', '徐', '何')
#     middle = ('芳', '军', '建', '明', '辉', '芬', '红', '丽', '功')
#     last = ('明', '芳', '', '民', '敏', '丽', '辰', '楷', '龙', '雪', '凡', '锋', '芝', '')
#     stuphone = ('110', '119', '120', '114')
#     stumajor = ('计算机科学与技术', '电子信息技术', '商务英语', '国际贸易', '金融')
#     stufaculty = ('信息管理与技术学院', '外国语学院', '会计学院', '国际金融学院')
#     stuadress = ('湖南省衡阳市', '湖南省长沙市', '湖南岳阳市',)
#     stu = StuInfo
#     for i in range(2000):
#         stu.stuname = r.choice(first) + r.choice(middle) + r.choice(last)
#         stu.stunum = '20170821' + r.randint(1000, 10000).__str__()
#         stu.stuphone = r.choice(stuphone)
#         stu.stubirth = r.randint(1995, 2003).__str__() + '-0' + r.randint(1, 9).__str__() + '-' + r.randint(1,
#                                                                                                             28).__str__()
#         stu.stusex = r.randint(0, 1)
#         stu.stuidcard = '43042619' + r.randint(95, 99).__str__() + r.randint(1, 12).__str__() + r.randint(1,
#                                                                                                           12).__str__() + r.randint(
#             1000, 9999).__str__()
#         stu.stumajor = r.choice(stumajor)
#         stu.stufaculty = r.choice(stufaculty)
#         stu.stuin = '20' + r.randint(16, 20).__str__() + '-09-01'
#         stu.stuadress = r.choice(stuadress)
#         stu.stubirth = stu.stubirth[0:10]
#         stu.stuin = stu.stuin[0:10]
#         print(stu.stunum)
#         stu.save()

class GetStuInfo(APIView):

    def get(self, request, *args, **kwargs):
        queryset = StuInfo.objects.all()
        # 获取GET请求参数
        pageNum = request.query_params.get('pageNum')
        pageSize = request.query_params.get('pageSize')
        stusex = request.query_params.get('stusex')
        stuname = request.query_params.get('stuname')
        stunum = request.query_params.get('stunum')
        # 模糊查询
        if not stunum == "":
            queryset = queryset.filter(stunum__contains=stunum)
        if not stuname == "":
            queryset = queryset.filter(stuname__contains=stuname)
        if not stusex == "":
            stusex = int(stusex)
            if stusex >=0:
                queryset = queryset.filter(stusex=stusex)
        # 分页
        paginator = Paginator(queryset, pageSize)  # 条数
        customer = paginator.page(pageNum)  # 页数

        stuinfo_data = AllStuinfoShowSerializer(customer, many=True)
        return Response({
            'code': 200,
            'msg': '请求成功',
            'total': queryset.count(),
            'data': stuinfo_data.data,
        })

class Stu(APIView):
    def get(self, request, *args, **kwargs):
        queryset = StuInfo.objects.all()
        # 获取GET请求参数
        pageNum = request.query_params.get('pageNum')
        pageSize = request.query_params.get('pageSize')
        stusex = request.query_params.get('stusex')
        stuname = request.query_params.get('stuname')
        stunum = request.query_params.get('stunum')
        # 模糊查询
        if not stunum == "":
            queryset = queryset.filter(stunum__contains=stunum)
        if not stuname == "":
            queryset = queryset.filter(stuname__contains=stuname)
        if not stusex == "":
            stusex = int(stusex)
            if stusex >= 0:
                queryset = queryset.filter(stusex=stusex)
        # 分页
        paginator = Paginator(queryset, pageSize)  # 条数
        customer = paginator.page(pageNum)  # 页数

        stuinfo_data = AllStuinfoShowSerializer(customer, many=True)
        return Response({
            'code': 200,
            'msg': '请求成功',
            'total': queryset.count(),
            'data': stuinfo_data.data,
        })

    def post(self, request):
        data = request.data
        stu = StuInfo()
        user = StuInfo.objects.filter(stunum=data.get('stunum')).first()
        if user:
            return Response({
                'code': '400',
                'msg': '学生已经存在',
            })
        stu.stunum = data.get('stunum')
        stu.stuname = data.get('stuname')
        stu.stuphone = data.get('stuphone')
        stu.stubirth = data.get('stubirth')
        stu.stusex = data.get('stusex')
        stu.stuidcard = data.get('stuidcard')
        stu.stumajor = data.get('stumajor')
        stu.stufaculty = data.get('stufaculty')
        stu.stuin = data.get('stuin')
        stu.stuadress = data.get('stuadress')
        stu.stubirth = stu.stubirth[0:10]
        stu.stuin = stu.stuin[0:10]
        stu.save()



        return Response({
            'code': 200,
            'msg': '成功添加',
        })
    #删除请求
    def delete(self,request):
        stunum = request.query_params.get('stunum')
        #删除
        stu = StuInfo.objects.filter(stunum=stunum).delete()
        if stu:
            return Response({
                'code': 200,
                'msg': '删除成功',
            })
        return Response({
            'code':100,
            'msg':'删除失败',

        })
# class addStu(APIView):
#     def post(self, request, *args, **kwargs):
#         serializer = AddStuinfoSerializer(data=request.data)
#         print(serializer.is_valid())
#         if serializer.is_valid():
#             print('失败')
#             return Response({
#                 'code': '400',
#                  'msg':'失败',
#             })
#         serializer.save()
#         print('成功添加')
#         return Response({
#             'code': 200,
#             'msg': '成功添加',
#         })
class editStu(APIView):
    def get(self,request,*args,**kwargs):
        stunum = request.query_params.get('stunum')
        stu = StuInfo.objects.filter(stunum=stunum).first()
        serializer = AllStuinfoShowSerializer(instance=stu,many=False)
        if serializer:
            return Response({
                'code':200,
                'msg':'请求成功',
                'data':serializer.data
            })
        return Response({
            'code': 100,
            'msg': '请求失败',
            'data': serializer.errors
        })
    def put(self,request,*args,**kwargs):
        # #print(request.data)
        # serializer = EditStuinfoSerializer(data=request.data,many=False)
        # serializer.is_valid()
        # serializer.save()
        # print(serializer.data)
        # return Response({
        #     'code':200
        # })
        data = request.data
        stu = StuInfo.objects.filter(stunum=data.get('stunum')).first()
        if stu:
            stu.stuname = data.get('stuname')
            stu.stuphone = data.get('stuphone')
            stu.stubirth = data.get('stubirth')
            stu.stusex = data.get('stusex')
            stu.stuidcard = data.get('stuidcard')
            stu.stumajor = data.get('stumajor')
            stu.stufaculty = data.get('stufaculty')
            stu.stuin = data.get('stuin')
            stu.stuadress = data.get('stuadress')
            stu.stubirth = stu.stubirth[0:10]
            stu.stuin = stu.stuin[0:10]
            stu.save()
            return Response({
                'code': 200,
                'msg': '修改成功',
            })
        return Response({
            'code':'error',
            'msg':'修改失败'
        })

