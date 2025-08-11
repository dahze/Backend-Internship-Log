from django.urls import path
from . import views

urlpatterns = [
    path('departments/', views.departments_list_create),
    path('departments/<int:pk>/', views.department_detail),
    path('courses/', views.courses_list_create),
    path('courses/<int:pk>/', views.course_detail),
    path('students/', views.students_list_create),
    path('students/<int:pk>/', views.student_detail),
]
