from django.shortcuts import render,HttpResponse
from api.utils.response import BaseResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models

#a.查看所有学位课并打印学位课名称以及授课老师
class DegreeCourseViews(APIView):

    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            DegreeCourse_list= models.DegreeCourse.objects.all().values('name','teachers__name')
            ret.data=DegreeCourse_list
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)


# b.查看所有学位课并打印学位课名称以及学位课的奖学金
class DegreeCourseScholarShipViews(APIView):

    def get(self,request,*args,**kwargs):
        ret = BaseResponse()
        try:
            DegreeCourse_list = models.DegreeCourse.objects.all().values('name','scholarship__value')
            print(DegreeCourse_list)
            ret.data = DegreeCourse_list
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)