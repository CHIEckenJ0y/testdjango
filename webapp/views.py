from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import DepartmentForm
from .forms import StudentForm
from .forms import CourseForm
from .forms import EnrollForm
from .forms import InstructorForm

def home_page(request):
    return render(request, 'pages/home.html')

def dashboard_page(request):
    enroll = Enrollment.objects.all()
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()
    return render(request, 'pages/dashboard.html', {'enroll': enroll, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def list_student_page(request):
    enroll = Enrollment.objects.all()
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()
    return render(request, 'pages/list_student.html', {'enroll': enroll, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def list_instructor_page(request):
    instructor = Instructor.objects.all()
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()
    return render(request, 'pages/list_instructor.html', {'instructor': instructor, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def list_courses_page(request):
    courses = Course.objects.all()
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()
    return render(request, 'pages/list_courses.html', {'courses': courses, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def list_department_page(request):
    department = Department.objects.all()
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()
    return render(request, 'pages/list_department.html', {'department': department, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def list_pre_enrolled_page(request):
    student = Student.objects.all()
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()
    return render(request, 'pages/list_pre_enrolled.html', {'student': student, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def edit_department_page(request, department_id):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()

    department = get_object_or_404(Department, pk=department_id)

    if request.method == 'POST':
        form = DepartmentForm(request.POST, instance=department)
        if form.is_valid():
            form.save()
            return redirect('list_department')  # Redirect to the department list page after successful update
    else:
        form = DepartmentForm(instance=department)
    return render(request, 'pages/edit_department.html',{'form': form,'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def add_department(request):
    if request.method == 'POST':
        department_name = request.POST.get('departmentName')
        if department_name:
            department = Department.objects.create(name=department_name)
            return JsonResponse({'success': True, 'department_name': department.name})
        else:
            return JsonResponse({'success': False, 'error': 'Department name cannot be empty'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

def check_department_exists(request):
    department_name = request.GET.get('department_name', None)

    # Logic para sa icheck if the department name already exists
    # For example, you can use your Department model:
    exists = Department.objects.filter(name=department_name).exists()

    return JsonResponse({'exists': exists})

def delete_department(request, department_id):
    department = Department.objects.all()
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()

    department = get_object_or_404(Department, pk=department_id)
    if request.method == 'POST':
        department.delete()
        return redirect('list_department')  # Redirect to the department list page after successful deletion

    return render(request, 'pages/delete_department.html', {'department': department, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def add_student_page(request):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('add_student') 
    else:
        form = StudentForm()
    return render(request, 'pages/add_student.html', {'form': form, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def add_course_page(request):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()
    form = CourseForm()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_courses')  
    else:
        form = CourseForm()
    return render(request, 'pages/add_course.html',{'form': form,'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def edit_courses_page(request, course_id):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()   

    course = get_object_or_404(Course, id=course_id)
    form = CourseForm(instance=course)

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('list_courses')

    else:
        form = CourseForm(instance=course)
    return render(request, 'pages/edit_course.html',{'form': form,'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def delete_course(request, course_id):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()  

    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        course.delete()
        return redirect('list_courses') 
    else:
        form = CourseForm(instance=course) 
    return render(request, 'pages/delete_course.html', {'form': form,'course': course, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def enroll_student_page(request):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()

    if request.method == 'POST':
        form = EnrollForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_student') 
    else:
        form = EnrollForm()
    return render(request, 'pages/enroll_student.html', {'form': form, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def delete_enrolled_student(request, enrolled_student_id):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count()  

    enrolled_student = get_object_or_404(Enrollment, id=enrolled_student_id)

    if request.method == 'POST':
        enrolled_student.delete()
        return redirect('list_student') 
    
    return render(request, 'pages/delete_enrolled_student.html', {'enrolled_student': enrolled_student, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def add_instructor(request):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count() 

    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_instructor')  
    else:
        form = InstructorForm()

    return render(request, 'pages/add_instructor.html', {'form': form, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def edit_instructor(request, instructor_id):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count() 

    instructor = get_object_or_404(Instructor, id=instructor_id)

    if request.method == 'POST':
        form = InstructorForm(request.POST, request.FILES, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('list_instructor')  
    else:
        form = InstructorForm(instance=instructor)

    return render(request, 'pages/edit_instructor.html', {'form': form, 'instructor': instructor, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def delete_instructor(request, instructor_id):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count() 

    instructor = get_object_or_404(Instructor, id=instructor_id)

    if request.method == 'POST':
        instructor.delete()
        return redirect('list_instructor') 

    return render(request, 'pages/delete_instructor.html', {'instructor': instructor, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def edit_pre_enrolled(request, student_id):
    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count() 

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            return redirect('list_pre_enrolled')
    else:
        form = StudentForm(instance=student)

    return render(request, 'pages/edit_pre_enrolled.html', {'form': form, 'student': student, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})

def delete_pre_enrolled(request, student_id):

    instructor_count = Instructor.objects.count()
    student_count = Enrollment.objects.count()
    course_count = Course.objects.count()
    department_count = Department.objects.count() 

    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('list_pre_enrolled') 

    return render(request, 'pages/delete_pre_enrolled.html', {'student': student, 'instructor_count': instructor_count ,'student_count': student_count,'course_count': course_count,'department_count': department_count})