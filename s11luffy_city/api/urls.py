from django.conf.urls import url
from api.views import course

# from api import views
#
#
# urlpatterns = [
#     # url(r'degreecourses/',views.Courses.as_view())
# ]
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'courses', views.Courses)
# urlpatterns += router.urls


urlpatterns = [
    # 查看课程列表接口
    url(r'courses/$', course.CoursesView.as_view()),

    # 查看课程列表详细接口
    url(r'courses/(?P<pk>\d+)/$', course.CourseDetailView.as_view()),

    # a.查看所有学位课并打印学位课名称和授课教师接口
    url(r'^a/$', course.DegreeCourseView.as_view()),

    # b.查看所有学位课并打印学位课名称以及学位课的奖学金
    url(r'^b/$', course.DegreeMoneyView.as_view()),

    # c. 展示所有的专题课
    url(r'^c/$', course.CourseView.as_view()),

    # d. 查看id=1的学位课对应的所有模块名称
    url(r'^d/$', course.CourseModuleView.as_view()),

    # e.获取id = 1的专题课，并打印：课程名、级别(中文)、why_study、what_to_study_brief、所有recommend_courses
    url(r'^e/$', course.CourseView1.as_view()),

    # f.获取id = 1的专题课，并打印该课程相关的所有常见问题
    url(r'^f/$', course.CourseQuesView2.as_view()),

    # g.获取id = 1的专题课，并打印该课程相关的课程大纲
    url(r'^g/$', course.CourseView3.as_view()),

    # h.获取id = 1的专题课，并打印该课程相关的所有章节
    url(r'^h/$', course.CourseView4.as_view())
]
