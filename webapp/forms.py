from django.forms import ModelForm
from .models import Department
from .models import Student
from .models import Course
from .models import Enrollment
from .models import Instructor
from django import forms

class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['name']

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'Age', 'date_of_birth', 'photo']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget = forms.DateInput(attrs={'type': 'date'})

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = ['course_code', 'course_name', 'department', 'instructor']

class EnrollForm(ModelForm):
    class Meta:
        model = Enrollment
        fields = ['student', 'course', 'year_level']

class InstructorForm(ModelForm):
    class Meta:
        model = Instructor
        fields = ['photo', 'name', 'department', 'email']




