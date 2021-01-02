

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from Stu.models import StuInfo
from User.UserSerializers import LoginSerializers
from User.models import User


class LoginView(APIView):

    def post(self, request):

        user = LoginSerializers(data=request.data)

        if user.is_valid():
            return Response({
                'code': status.HTTP_200_OK,
                'msg': request.data.get('username'),
                'data': {

                }
            });
        print(user.errors)
        return Response({
            'code': 201,
            'msg': user.errors
        })
