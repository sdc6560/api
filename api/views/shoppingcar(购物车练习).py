import redis

from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin

from api.utils.response import BaseResponse


CONN = redis.Redis(host='192.168.11.61',port=6379)

class ShoppingCarView(ViewSetMixin,APIView):
    def list(self,request,*args,**kwargs):
        CONN.hset('sdc_xxz','k1','ssss')
        CONN.hset('sdc_xxz','k2','6666')
        n1 = CONN.hget('sdc_xxz','k1').decode('utf8')
        n2 = CONN.hget('sdc_xxz','k2').decode('utf8')
        print(n1,n2)


        return HttpResponse('ok')

    def create(self, request, *args, **kwargs):

        return HttpResponse('ok')