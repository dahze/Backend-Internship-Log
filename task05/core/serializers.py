from rest_framework import serializers
from .models import Department, Course, Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'course']

class CourseSerializer(serializers.ModelSerializer):
    students = StudentSerializer(many=True, read_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all())

    class Meta:
        model = Course
        fields = ['id', 'name', 'department', 'students']

class DepartmentSerializer(serializers.ModelSerializer):
    courses = CourseSerializer(many=True, read_only=True)

    class Meta:
        model = Department
        fields = ['id', 'name', 'courses']
