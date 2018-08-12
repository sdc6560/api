from django.conf.urls import url
from api.views import course
from api.views import shoppingcar
# from api.views import degreecourse


urlpatterns = [

    url(r'courses/$', course.CoursesView.as_view({'get': 'list', 'post': 'create'})),
    url(r'courses/(?P<pk>\d+)/$', course.CoursesView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'})),
    url(r'shoppingcar/$', shoppingcar.ShoppingCarView.as_view({'get': 'list', 'post': 'create','delete':'destroy','put':'update'}))
]