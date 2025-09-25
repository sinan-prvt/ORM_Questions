from django.shortcuts import render
from .models import Course, Student
from django.db.models import Count, Avg, Sum, Max
from django.db.models import F
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned


def index(request):
    return render(request, 'index.html')


#=================================== get() Method ============================================== 


#-------------- Fetch by primary key

# def student_detail(request):
#     try:
#         student = Student.objects.get(id=1)
#     except ObjectDoesNotExist:
#         student = None
#     return render(request, 'student_details.html', {'student': student})



#-------------- Fetch by Unique Field

# def student_detail(request):
#     try:
#         student = Student.objects.get(name="Affan")
#     except ObjectDoesNotExist:
#         student = None
#     return render(request, 'student_details.html', {'student': student})



#-------------- Multiple Conditions

# def student_detail(request):
#     try:
#         student = Student.objects.get(name="Sinan", age=19)
#     except Student.DoesNotExist:
#         student = None
#     except Student.MultipleObjectsReturned:
#         student = None
#     return render(request, 'student_details.html', {'student': student})



#-------------- get_or_create() – Avoids exception by creating if not found

def student_detail(request):
    student, created = Student.objects.get_or_create(age=22)
    return render(request, 'student_details.html', {'student': student, 'created': created} )





#=================================== filter() Method ============================================== 


#-------------- Filter by One Field

# def student_filter(request):
#     students = Student.objects.filter(age=19)
#     return render(request, 'student_filter.html', {'students': students})


#-------------- Multiple filters

# def student_filter(request):
#     student = Student.objects.filter(name="Affan", age=24)
#     return render(request, 'student_filter.html', {'student': student})



#-------------- lookup expressions

# def student_filter(request):
#     # students = Student.objects.filter(age__gt = 21)
#     # students = Student.objects.filter(age__lt = 21)
#     # students = Student.objects.filter(name__contains="na")
#     # students = Student.objects.filter(name__startswith="A")
#     students = Student.objects.filter(age__in=[19,23,20])
#     return render(request, 'student_filter.html', {'students': students})



#-------------- Chaining filters

# def student_filter(request):
#     students = Student.objects.filter(age__gt=21).filter(name__icontains='an')
#     return render(request, 'student_filter.html', {'students': students})



#-------------- Using exclude() with filter()

def student_filter(request):
    students = Student.objects.filter(age__gt=21).exclude(name="Affan")
    return render(request, 'student_filter.html', {'students': students})




#=================================== exclude() Method ============================================== 







def course_list(request):
    courses = Course.objects.annotate(student_count=Count('student'))
    return render(request, 'courses_list.html', {'courses': courses})


# def course_list(request):
#     courses = Course.objects.annotate(avg_age=Avg('student__age'))
#     return render(request, 'courses_list.html', {'courses': courses})


# def course_list(request):
#     courses = Course.objects.annotate(max_age=Max('student__age'))
#     return render(request, 'courses_list.html', {'courses': courses})

# def course_list(request):
#     courses = Course.objects.annotate(student_count=Sum('student'))
#     return render(request, 'courses_list.html', {'courses': courses})


# def course_list(request):
#     courses = Course.objects.annotate(student_count=Count('student'),
#                                       max_age=Max('student__age'),
#                                       avg_age=Avg('student__age')
#                                       )
#     return render(request, 'courses_list.html', {'courses': courses})




# def course_list(request):
#     courses = Student.objects.aggregate(avg_age=Avg('age'))
#     return render(request, 'courses_list.html', {'courses': courses})


# def course_list(request):
#     courses = Student.objects.aggregate(sum_age=Sum('age'))
#     return render(request, 'courses_list.html', {'courses':courses})

# def course_list(request):
#     courses = Student.objects.aggregate(max_age=Max('age'))
#     return render(request, 'courses_list.html', {'courses': courses})

# def course_list(request):
#     courses = Student.objects.aggregate(avg_age=Avg('age'),
#                                         sum_age=Sum('age'),
#                                         max_age=Max('age')
#                                         )
#     return render(request, 'courses_list.html', {'courses': courses})


# def course_list(request):
#     students = Student.objects.values()
#     return render(request, 'courses_list.html', {'students': students})


# def course_list(request):
#     students = Student.objects.filter(age__gt=22).values('name')
#     return render(request, 'courses_list.html', {'students': students})


# def course_list(request):
#     students = Student.objects.values('name','age').order_by('age')
#     return render(request, 'courses_list.html', {'students': students})


# def course_list(request):
#     students = Student.objects.values_list()
#     return render(request, 'courses_list.html', {'students': students})


# def course_list(request):
#     students = Student.objects.filter(age__gt=22).values_list('name', flat=True)
#     return render(request, 'courses_list.html', {'students': students})


# def course_list(request):
#     students = Student.objects.filter(age__gt=21).values_list('name', 'course').order_by('age')
#     return render(request, 'courses_list.html', {'students': students})


# def course_list(request):
#     students = Student.objects.update(age=F('age') + 1)
#     students = Student.objects.all()
#     return render(request, 'courses_list.html', {'students': students})

# def course_list(request):
#     course = Course.objects.get(title='Python')
#     Student.objects.filter(course=course).update(age=F('age') + 2)
#     students = Student.objects.all()
#     return render(request, 'courses_list.html', {'students': students})

