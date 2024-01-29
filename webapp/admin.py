from django.contrib import admin
from .models import Student, Department, Instructor, Course, Enrollment

# Register your models here.

admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Instructor)
admin.site.register(Course)
admin.site.register(Enrollment)
