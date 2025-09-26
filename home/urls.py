from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses_list', views.course_list, name='courses_list'),
    path("student_get/", views.student_get, name="student_get"),
    path("student_filter/", views.student_filter, name="student_filter"),
    path("student_exclude/", views.student_exclude, name="student_exclude"),
]
