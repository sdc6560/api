from django.conf.urls import url
from api.views import course
from api.views import degreecourse


urlpatterns = [

    url(r'^courses/$',course.CoursesView.as_view()),
    url(r'^courses1/(?P<pk>.+)',course.CoursesView1.as_view()),
    url(r'^courses2/(?P<pk>.+)',course.CoursesView2.as_view()),
    url(r'^courses3/(?P<pk>.+)',course.CoursesView3.as_view()),
    url(r'^courses4/(?P<pk>.+)',course.CoursesView4.as_view()),
    url(r'courses/(?P<pk>.+)',course.CoursesIdView.as_view()),
    url(r'^degreecourse/$',degreecourse.DegreeCourseViews.as_view()),
    url(r'^degreecoursescholarship/$',degreecourse.DegreeCourseScholarShipViews.as_view())
]