"""AssignmentPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from .views import (AssignmentListView, 
LectureListView, 
studentAssignmentListView, 
StudentLectureListView, 
studentColleagueListView, responseListView, 
studentNewAssignmentListView,
AssignmentDetailView,
StudentsListView)
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required


urlpatterns = [
    #path('', views.index, name=''),
    path('', views.studentLogin, name='login'),
    path('logout/', views.studentLogout, name='logout'),
     path('lecturer/logout', views.lecturerLogout, name='lecturer/logout'),
    path('register/', views.studentRegister, name='register'),
    path('student/view_assignment', login_required(views.studentAssignmentListView.as_view()), name='view-assignment'),
    path('student/profile', views.studentProfile, name='student_profile'),
    path('student/colleagues', login_required(views.studentColleagueListView.as_view()), name='student_colleague'),
    path('student/new_assignment', login_required(views.studentNewAssignmentListView.as_view()), name='new_assignment'),
    path('student/<str:slug>/assignment_details', views.submitAssignment, name='assignment_response'),
    path('lecturer/', views.lecturerLogin, name='lecturer/login'),
    path('lecturer/register', views.lecturerRegister, name='lecturer/register'),
    path('dashboard/', views.home, name='dashboard'),
    path('lecturer/dashboard', views.lecturer_home, name='lecturer/dashboard'),
    path('lecturer/add_assignment', views.addAssignment, name='add_assignment'),
    path('lecturer/add_lecture', views.addLecture, name='add_lecture'),
    path('lecturer/<str:slug>/assignment_details', login_required(AssignmentDetailView.as_view()), name='assignment_details'),
    path('lecturer/<str:slug>/grade_assignment', views.grade, name='grade_assignment'),
    path('lecturer/view_assignment', login_required(AssignmentListView.as_view()), name='view_assignment'),
    path('lecturer/recieved_assignment', responseListView, name='recieved_assignment'),
    path('lecturer/all_students', login_required(StudentsListView.as_view()), name='all_students'),
    path('lecturer/view_lectures', login_required(LectureListView.as_view()), name='view_lectures'),
    path('lecturer/<str:slug>/edit_lecture', views.updateLecture, name='lecture_edit'),
    path('student/view_lectures', login_required(StudentLectureListView.as_view()), name='student/view_lecture'),
    path('lecturer/<str:slug>/update', views.updateAssignment, name='assignment_edit'),
    path('lecturer/<str:slug>/delete', views.deleteAssignment, name='assignment_delete'),
    path('student/faq', views.faq, name='faq'),
    path('student/forum', views.forum, name='forum'),
 ]
