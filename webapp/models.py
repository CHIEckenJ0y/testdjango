from django.db import models

# Create your models here.

class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Instructor(models.Model):
    name = models.CharField(max_length=50, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    photo = models.ImageField(upload_to='albums/', blank=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True)
    course_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"


class Student(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=50, null=True)
    Age = models.IntegerField(null=True)
    date_of_birth = models.DateField(null=True)
    #courses = models.ManyToManyField(Course, through='Enrollment')
    #course = models.ForeignKey(Course, on_delete=models.CASCADE, default=1)
    photo = models.ImageField(upload_to='albums/', blank=True)
    

    def __str__(self):
        return f"{self.first_name} {self.middle_name} {self.last_name}"


class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year_level = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} enrolled in {self.course} with {self.year_level} year level "