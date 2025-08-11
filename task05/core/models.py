from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='courses')

    class Meta:
        unique_together = ('name', 'department')

    def __str__(self):
        return f"{self.name} ({self.department.name})"

class Student(models.Model):
    name = models.CharField(max_length=255)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return f"{self.name} - {self.course.name}"
