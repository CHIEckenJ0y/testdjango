from django.urls import path
from .views import add_department
from .views import delete_department
from .views import delete_course
from .views import delete_instructor
from .views import delete_enrolled_student
from .views import delete_pre_enrolled
from .views import add_instructor
from .views import edit_instructor
from .views import edit_pre_enrolled
from . import views

urlpatterns = [
    path('', views.home_page, name='homePage'),
    path('pages/dashboard/', views.dashboard_page, name='dashboard'),
    path('pages/list_student/', views.list_student_page, name='list_student'),
    path('pages/list_instructor/', views.list_instructor_page, name='list_instructor'),
    path('pages/list_courses/', views.list_courses_page, name='list_courses'),
    path('pages/list_department/', views.list_department_page, name='list_department'),
    path('pages/list_pre_enrolled/', views.list_pre_enrolled_page, name='list_pre_enrolled'),
    
    path('pages/add_student/', views.add_student_page, name='add_student'),
    path('pages/edit_pre_enrolled/<int:student_id>/', edit_pre_enrolled, name='edit_pre_enrolled'),

    path('pages/enroll_student/', views.enroll_student_page, name='enroll_student'),
    path('delete_enrolled_student/<int:enrolled_student_id>/', delete_enrolled_student, name='delete_enrolled_student'),
    path('delete_pre_enrolled/<int:student_id>/', delete_pre_enrolled, name='delete_pre_enrolled'),

    path('pages/add_course/', views.add_course_page, name='add_course'),
    path('pages/edit_course/<int:course_id>/', views.edit_courses_page, name='edit_course'),
    path('delete_course/<int:course_id>/', delete_course, name='delete_course'),

    path('pages/add_instructor/', add_instructor, name='add_instructor'),
    path('edit_instructor/<int:instructor_id>/', edit_instructor, name='edit_instructor'),
    path('delete_instructor/<int:instructor_id>/', delete_instructor, name='delete_instructor'),

    path('pages/edit_department/<int:department_id>/', views.edit_department_page, name='edit_department'),
    path('delete_department/<int:department_id>/', delete_department, name='delete_department'),

    # to add value
    path('add_department/', add_department, name='add_department'),

    # I add this for cheking a value if exist
    path('check_department_exists/', views.check_department_exists, name='check_department_exists'),
]
