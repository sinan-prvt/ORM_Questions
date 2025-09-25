from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses_list', views.course_list, name='courses_list'),
    path("student_detail/", views.student_detail, name="student_detail"),
    path("student_filter/", views.student_filter, name="student_filter"),
]
