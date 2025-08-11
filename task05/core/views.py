from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Department, Course, Student
from .serializers import DepartmentSerializer, CourseSerializer, StudentSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def departments_list_create(request):
    if request.method == 'GET':
        qs = Department.objects.all().order_by('name')
        serializer = DepartmentSerializer(qs, many=True)
        return Response(serializer.data)

    serializer = DepartmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def department_detail(request, pk):
    dept = get_object_or_404(Department, pk=pk)

    if request.method == 'GET':
        serializer = DepartmentSerializer(dept)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = DepartmentSerializer(dept, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    dept.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def courses_list_create(request):
    if request.method == 'GET':
        dept_id = request.query_params.get('department')
        qs = Course.objects.all().order_by('name')
        if dept_id:
            qs = qs.filter(department_id=dept_id)
        serializer = CourseSerializer(qs, many=True)
        return Response(serializer.data)

    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)

    if request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    course.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def students_list_create(request):
    if request.method == 'GET':
        course_id = request.query_params.get('course')
        search = request.query_params.get('search')
        qs = Student.objects.all().order_by('name')
        if course_id:
            qs = qs.filter(course_id=course_id)
        if search:
            qs = qs.filter(name__icontains=search)
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)

    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    if request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    student.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
