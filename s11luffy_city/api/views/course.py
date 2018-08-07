from django.shortcuts import render, HttpResponse
# from django.views import View
from rest_framework.viewsets import ModelViewSet
from api import serializers as app01_serializers
import json
from rest_framework.views import APIView
from api.models import CourseCategory, CourseSubCategory, \
    DegreeCourse, Teacher, Scholarship, Course, CourseDetail, OftenAskedQuestion, \
    CourseOutline, CourseChapter, CourseSection, CourseSection, CourseSection

# class CoursesView(ModelViewSet):
#     queryset=Course.objects.all()
#     serializer_class =app01_serializers.Course_serializers


import json
from django.shortcuts import HttpResponse
from django.http import JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.versioning import URLPathVersioning
from rest_framework.pagination import PageNumberPagination

from api import models
from api.serializers.course import CourseSerializer
from api.utils.response import BaseResponse


# 获取课程列表接口

class CoursesView(APIView):

    def get(self, request, *args, **kwargs):
        # response = {'code':1000,'data':None,'error':None}
        ret = BaseResponse()
        try:
            # 从数据库获取数据
            queryset = models.Course.objects.all()

            # 分页
            page = PageNumberPagination()
            course_list = page.paginate_queryset(queryset, request, self)

            # 分页之后的结果执行序列化
            ser = CourseSerializer(instance=course_list, many=True)

            ret.data = ser.data
        except Exception as e:
            ret.code = 500
            ret.error = '获取数据失败'

        return Response(ret.dict)


# 获取课程详细接口
class CourseDetailView(APIView):
    def get(self, request, pk, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.get(id=pk)
            ser = CourseSerializer(instance=course)
            response['data'] = ser.data
        except Exception as e:
            response['code'] = 500
            response['error'] = '获取数据失败'
        return Response(response)


# a.查看所有学位课并打印学位课名称和授课教师姓名接口
class DegreeCourseView(APIView):
    def get(self, request, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.DegreeCourse.objects.all().values('name', 'teachers__name')
            response['data'] = course
        except Exception as e:
            response['code'] = 500
            response['error'] = '数据获取失败'
        return Response(response)

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金


class DegreeMoneyView(APIView):
    def get(self, request, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.DegreeCourse.objects.all().values('name', 'scholarship__value')
            response['data'] = course
        except Exception as e:
            response['code'] = 500
            response['error'] = '数据获取失败'
        return Response(response)


# c. 展示所有的专题课
class CourseView(APIView):
    def get(self, request, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.all().values('name')
            response['data'] = course
        except Exception as e:
            response['code'] = 500
            response['error'] = '数据获取失败'
        return Response(response)


# d. 查看id=1的学位课对应的所有模块名称
class CourseModuleView(APIView):
    def get(self, request, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.DegreeCourse.objects.filter(id=1).values('course__name')
            response['data'] = course
        except Exception as e:
            response['code'] = 500
            response['error'] = '数据获取失败'
        return Response(response)


# e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
class CourseView1(APIView):
    def get(self, request, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.filter(id=1).values('name', 'level', 'coursedetail__why_study',
                                                               'coursedetail__what_to_study_brief',
                                                               'coursedetail__recommend_courses')
            response['data'] = course
        except Exception as e:
            response['code'] = 500
            response['error'] = '数据获取失败'
        return Response(response)


# f.获取id = 1的专题课，并打印该课程相关的所有常见问题
class CourseQuesView2(APIView):
    def get(self, request, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.filter(id=1).values('asked_question')
            response['data'] = course
        except Exception as e:
            response['code'] = 500
            response['error'] = '数据获取失败'
        return Response(response)


# g.获取id = 1的专题课，并打印该课程相关的课程大纲
class CourseView3(APIView):
    def get(self, request, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.filter(id=1).values('coursedetail__courseoutline__title')
            response['data'] = course
        except Exception as e:
            response['code'] = 500
            response['error'] = '数据获取失败'
        return Response(response)


# h.获取id = 1的专题课，并打印该课程相关的所有章节
class CourseView4(APIView):
    def get(self, request, *args, **kwargs):
        response = {'code': 1000, 'data': None, 'error': None}
        try:
            course = models.Course.objects.filter(id=1).values('coursechapters__name')
            response['data'] = course
        except Exception as e:
            response['code'] = 500
            response['error'] = '数据获取失败'
        return Response(response)
