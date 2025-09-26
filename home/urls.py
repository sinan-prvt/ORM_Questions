from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("student_get/", views.student_get, name="student_get"),
    path("student_filter/", views.student_filter, name="student_filter"),
    path("student_exclude/", views.student_exclude, name="student_exclude"),
    path("student_lookup/", views.student_lookup, name="student_lookup"),
    path("student_q/", views.student_q, name="student_q"),
    path('student_annotate/', views.student_annotate, name='student_annotate'),
    path('student_aggregate/', views.student_aggregate, name='student_aggregate'),
    path('student_value/', views.student_value, name='student_value'),
]
