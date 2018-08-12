from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from api.utils.response import BaseResponse
from api import models

SHOPPING_CAR={}
class CoursesView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        ret = BaseResponse()

        return HttpResponse('ok')

    def create(self, request, *args, **kwargs):
        ret = BaseResponse()
        res1={}
        res=request.POST
        user_id=res.get('user_id')
        course_id = res.get('course_id')
        price = res.get('price')
        res1['course_id']=course_id
        res1['price']=price
        SHOPPING_CAR[user_id] = res1

        for i in SHOPPING_CAR.keys():

            obj = models.Course.objects.filter(pk=1).first()
            price_list=obj.price_policy.all()
            print(type(price_list),price_list)
            if price in price_list:
                SHOPPING_CAR[user_id][price_list]=price_list
            else:
                return HttpResponse('no')
        return HttpResponse('ok')