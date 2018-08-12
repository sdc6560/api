from django.shortcuts import render,HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.request import Request
from api.utils.response import BaseResponse
from api import models
"""

		
"""

# c.展示所有的专题课
class CoursesView(APIView):

    def get(self,request,*args,**kwargs):
        ret=BaseResponse()
        try:
            courses_list = models.Course.objects.filter(degree_course__isnull=False).values('name')
            ret.data=courses_list
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)
# d. 查看id=1的学位课对应的所有模块名称
class CoursesIdView(APIView):

    def get(self,request,pk,*args,**kwargs):
        ret = BaseResponse()
        print(pk)
        try:
            # courses_list = models.Course.objects.filter(pk=pk,egree_course__isnull=True).values('name')
            courses_list = models. Course.objects.filter(degree_course_id=1).values()
            ret.data = courses_list
            print(courses_list)
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)


# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
class CoursesView1(APIView):
    def get(self,request,pk,*args,**kwargs):
        ret=BaseResponse()
        res={}
        try:
            courses_obj = models.Course.objects.filter(pk=pk, degree_course__isnull=False).first()
            print(courses_obj)
            res['name'] = courses_obj.name
            res['brief'] = courses_obj.brief
            res['level'] = courses_obj.get_level_display()
            res['hours'] = courses_obj.coursedetail.hours
            res['why_study'] = courses_obj.coursedetail.why_study

            name_list = courses_obj.coursedetail.recommend_courses.all()
            list = []
            for i in name_list:
                print('___>',i.name)
                list.append(i.name)
            res['name_list'] = list
            print(res)
            ret.data = res
            print(ret.dict)
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'
        return Response(ret.dict)


# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
class CoursesView2(APIView):
    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()


        try:
            courses_list = models.Course.objects.filter(pk=pk,
                                                        degree_course__isnull=False).first().asked_question.all().values(
                'question')
            ret.data = courses_list
            print(courses_list)
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'


        return Response(ret.dict)


# g.获取id = 1的专题课，并打印该课程相关的课程大纲
class CoursesView3(APIView):
    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()


        try:
            courses_list = models.Course.objects.filter(pk=pk,
                                                        degree_course__isnull=False).values('coursedetail__courseoutline__title')
            ret.data = courses_list
            print(courses_list)
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'


        return Response(ret.dict)

# h.获取id = 1的专题课，并打印该课程相关的所有章节
class CoursesView4(APIView):
    def get(self, request, pk, *args, **kwargs):
        ret = BaseResponse()

        try:
            courses_list = models.Course.objects.filter(pk=pk,
                                                        degree_course__isnull=False).values('coursechapters__name')
            ret.data = courses_list
            print(courses_list)
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)