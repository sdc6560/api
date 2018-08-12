import redis

from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSetMixin
from rest_framework.response import Response
from django.conf import settings
import json

from api import models
from api.utils.response import BaseResponse


CONN=redis.Redis(host='192.168.11.151',port=6379)

class ShoppingCarView(ViewSetMixin,APIView):

    def list(self,request,*args,**kwargs):
        ret = BaseResponse()
        shopping_car_course_list = []

        # pattern = "shopping_car_%s_*" % (USER_ID,)
        pattern = settings.LUFFY_SHOPPING_CAR % (1, '*',)

        user_key_list = CONN.keys(pattern)
        for key in user_key_list:
            temp = {
                'id': CONN.hget(key, 'id').decode('utf-8'),
                'name': CONN.hget(key, 'name').decode('utf-8'),
                'img': CONN.hget(key, 'img').decode('utf-8'),
                'default_price_id': CONN.hget(key, 'default_price_id').decode('utf-8'),
                'price_policy_dict': json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
            }
            shopping_car_course_list.append(temp)

        ret.data = shopping_car_course_list

        return Response(ret.dict)

    def create(self, request, *args, **kwargs):
        ret = BaseResponse()
        # print(request.data)
        # user_id = request.data.get('user_id')
        course_id = request.data.get('course_id')
        price_id = request.data.get('price_id')
        course_obj = models.Course.objects.filter(pk=course_id).first()
        if not course_obj:
            ret.code = 10001
            ret.error = '课程不存在'
            return Response(ret.dict)
        price_policy_queryset = course_obj.price_policy.all()
        price_policy_dict = {}
        for item in price_policy_queryset:
            temp = {
                'id': item.id,
                'price': item.price,
                'valid_period': item.valid_period,
                'valid_period_display': item.get_valid_period_display()
            }
            price_policy_dict[item.id] = temp
        if price_id not in price_policy_dict:
            ret.code = 10002
            ret.error = '价格策略不存在'
            return Response(ret.dict)
        key = settings.LUFFY_SHOPPING_CAR % (1, '*',)
        keys = CONN.keys(key)
        if keys and len(keys) >= 1000:
            ret.code = 10003
            ret.error = '购物车已经满了，请先结算'
            return Response(ret.dict)
        key = settings.LUFFY_SHOPPING_CAR % (1, course_id,)
        CONN.hset(key, 'id', course_id)
        CONN.hset(key, 'name', course_obj.name)
        CONN.hset(key, 'img', course_obj.course_img)
        CONN.hset(key, 'default_price_id', price_id)
        CONN.hset(key, 'price_policy_dict', json.dumps(price_policy_dict))

        CONN.expire(key, 20 * 60)
        ret.code = 10004
        ret.data = '购买成功'
        return Response(ret.dict)

    def destroy(self, request, *args, **kwargs):
        ret = BaseResponse()
        course_id = request.data.get('course_id')
        price_id = request.data.get('price_id')
        key = settings.LUFFY_SHOPPING_CAR % (1, course_id,)

        if not CONN.exists(key):
            ret.code = 10007
            ret.error = '课程不存在'
            return Response(ret.dict)

        price_policy_dict = json.loads(CONN.hget(key, 'price_policy_dict').decode('utf-8'))
        if price_id not in price_policy_dict:
            ret.code = 10008
            ret.error = '价格策略不存在'
            return Response(ret.dict)

        CONN.hset(key, 'default_price_id', price_id)
        CONN.expire(key, 20 * 60)
        ret.data = '修改成功'
        return Response(ret.dict)
    def update(self, request, *args, **kwargs):
        ret = BaseResponse()
        course_id = request.data.get('course_id')
        key = settings.LUFFY_SHOPPING_CAR % (1, course_id)
        CONN.delete(key)
        ret.data = '删除成功'
        return Response(ret.dict)