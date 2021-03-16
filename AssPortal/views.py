from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, Http404, redirect
from .models import Lecturer, Lecture, Assignment, assResponse, Student, Grade
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.models import User
from .forms import (StudentRegForm, LecturerRegForm, 
addAssignmentForm, addLectureForm, 
submitAssignmentForm, userUpdateProfileForm, 
studentUpdateProfileForm, ResponseForm)
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.conf import settings
from django.forms import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone , dateformat
import datetime
from django.urls import reverse_lazy
from django.db.models import Q


# Create your views here.


def studentRegister(request):
    form = StudentRegForm()
    if request.method == 'POST':
        form = StudentRegForm(request.POST, request.FILES)
        if form.is_valid():
            stud = form.cleaned_data.get('first_name')
            student_obj = form.save(commit=False)
            student_obj.user = User.objects.create_user(
                password = form.cleaned_data.get('password2'),
                username = form.cleaned_data.get('username'),
                
            )
            student_obj.save()
            messages.success(request, 'Account for ' + stud + ' was created successfully!')
    else:
       form = StudentRegForm()
    return render(request, 'register.html', context = {'form':form})



def studentLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        student = authenticate(request, username = username, password = password)
        try:
            if student is not None:
                if student.student.is_student:
                    login(request, student)
                    return redirect('dashboard')

            else:
                messages.error(request, 'Username or Password not correct!')
        except:
            messages.error(request, 'invalid login details')
            return redirect('login')
    return render(request, 'login.html')

def studentLogout(request):
    logout(request)
    return redirect('login')


# def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context["date_expired"] = datetime.date.today()
#     return context

@login_required(login_url= 'login')
def home(request):

    today = datetime.date.today()

    total_lecture = Lecture.objects.filter(level = request.user.student.level).count()
    new_assignment = Assignment.objects.filter(level = request.user.student.level, is_viewed=False, due_date__gte = today).count()
    total_course_mate = Student.objects.filter(level = request.user.student.level).count()
    total_assignment = Assignment.objects.filter(level = request.user.student.level).count()

    context = {
        'total_lecture': total_lecture,
        'total_assignment': total_assignment,
        'new_assignment' : new_assignment,
        'total_course_mate': total_course_mate,

    }


    
    return render(request, 'student/home.html', context)
            
            
def lecturerRegister(request):
    signup = LecturerRegForm()
    if request.method == 'POST':    
        signup = LecturerRegForm(request.POST, request.FILES)
        if signup.is_valid():
            lecturer = signup.cleaned_data.get('first_name')
            lecturer_obj = signup.save(commit=False)
            lecturer_obj.user = User.objects.create_user(
                password = signup.cleaned_data.get('password2'),
                username = signup.cleaned_data.get('username'),
                
            )
            lecturer_obj.save()
            messages.success(request, 'Account for ' + lecturer + ' was created successfully!')
    else:
        signup = LecturerRegForm()
    return render(request, 'lecturer/register.html', context = {'signup' : signup})

def lecturerLogout(request):
    logout(request)
    return redirect('lecturer/login')

def lecturerLogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        lecturer = authenticate(request, username = username, password = password)
        try:

            if lecturer is not None:
                login(request, lecturer)
                if lecturer.lecturer.is_student == False:
                    return redirect('lecturer/dashboard')
            else:
                messages.error(request, 'Username or Password not correct!')
        except:
            messages.error(request, 'Invalaid login detail ):')
            return redirect("lecturer/login")
    return render(request, 'lecturer/login.html')
            
@login_required(login_url= 'lecturer/login')
def lecturer_home(request):

    assignment = Assignment.objects.all()
    lecture = Lecture.objects.all()
    total_assignment = Assignment.objects.filter(lecturer = request.user).count()
    total_lecture = Lecture.objects.count()
    total_student = Student.objects.count()
    submitted_assignment = assResponse.objects.select_related('question').filter(lecturer = request.user, is_accessed = False).count()

    context = {
        'assignmet': assignment,
        'lecture': lecture,
        'total_assignment': total_assignment,
        'total_lecture': total_lecture,
        'total_student': total_student,
        'submitted_assignment' : submitted_assignment
    }

    
    return render(request, 'lecturer/home.html', context)



@login_required(login_url= 'lecturer/login')
def addAssignment(request):
    if request.method == 'POST':
        form = addAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.lecturer = request.user
            ass = form.cleaned_data.get('course_code')
            form.save()
            messages.success(request, 'Assignment for ' + str(ass) + ' added successfully!')
            return redirect('view_assignment')
    else:
       form = addAssignmentForm()
    return render(request, 'lecturer/add_assignment.html', context = {'form':form}) 

@login_required(login_url= 'login')
def submitAssignment(request, slug): 
    qs = Assignment.objects.get(slug=slug)
    form = submitAssignmentForm()
    if request.method == 'POST':
        level = request.POST['level']
        lecturer = request.POST['lecturer']
        matric_no = request.POST['matric_no']
        course_code = request.POST['course_code']
        question = request.POST['question']
        form = submitAssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            ass = form.save(commit=False)
            ass.question = question
            ass.lecturer = lecturer
            ass.level = level
            ass.matric_no = request.user.student.matric_no
            ass.course_code = course_code
            ass.save()
            qs.is_viewed = True
            qs.save()
            messages.success(request, f' {qs.course_code} Assignment Submitted successfully!')
            return redirect('new_assignment')
    else:
       form = submitAssignmentForm()

    return render(request, 'student/assignment_details.html', context = {'form':form, 'qs':qs})

@login_required(login_url= 'login')
def grade(request, slug):
    qs = assResponse.objects.get(slug=slug)
    form = ResponseForm()
    if request.method == 'POST':
        level = request.POST['level']
        question = request.POST['question']
        response = request.POST['response']
        matric_no = Student.objects.get(matric_no=qs.matric_no)
        course_code = request.POST['course_code']
        form = ResponseForm(request.POST)
        if form.is_valid():
            form.instance.lecturer = request.user.lecturer
            ass = form.save(commit=False)
            ass.question = question
            ass.level = level
            ass.student = matric_no
            ass.response = response
            ass.course_code = course_code
            ass.save()
            qs.is_accessed = True
            qs.save()
            messages.success(request, f'{qs} Graded Successfully!')
            return redirect('recieved_assignment')
    else:
       form = ResponseForm()

    return render(request, 'lecturer/grade_assignment.html', context = {'form':form, 'qs':qs})    


class AssignmentListView(ListView):
    template_name = 'lecturer/view_assignment.html'
    context_object_name = 'assignments'
    ordering = ['-date_uploaded']
    paginate_by = 10
    slug_field = 'slug_course_code'
    slug_url_kwargs = 'slug_course_code'

    def get_queryset(self):
        qs = Assignment.objects.filter(lecturer = self.request.user)
        return qs


def responseListView(request):
    qs = assResponse.objects.filter(lecturer=request.user)
    name = 'lecturer/received_assignments.html'
    context = {
        'response':qs
    }
    return render(request, name, context)



#     def form_valid(self, form):
#         form.instance.lecturer = self.request.user
#         return super().form_valid(form)


class studentAssignmentListView(ListView):
    template_name = 'student/view_assignment.html'
    context_object_name = 'assignments'
    ordering = ['-date_uploaded']
    

    def get_queryset(self):
        query = Assignment.objects.filter(level = self.request.user.student.level)
        qb = Grade.objects.filter(student=self.request.user.student)
        queryset = zip(query, qb)
        return queryset


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date_expired"] = datetime.date.today()
        return context
    

class studentNewAssignmentListView(ListView):
    template_name = 'student/new_assignment.html'
    context_object_name = 'assignments'
    ordering = ['-date_uploaded']

    def get_queryset(self):
        qs = Assignment.objects.filter(level=self.request.user.student.level, is_viewed = False, due_date__gte = timezone.now())
        return qs
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["date_expired"] = datetime.date.today()
        return context

class AssignmentDetailView(DetailView):
    
    template_name = 'lecturer/assignment_details.html'

    def get_queryset(self):
        qs = assResponse.objects.all()
        return qs


class studentColleagueListView(ListView):
    template_name = 'student/colleagues.html'
    context_object_name = 'colleagues'
    ordering = ['-date_joined']
    # paginate_by = 10

    def get_queryset(self):
        qs = Student.objects.filter(level=self.request.user.student.level)
        return qs

class StudentsListView(ListView):
    template_name = 'lecturer/all_students.html'
    context_object_name = 'students'
    ordering = ['-date_joined']
    # paginate_by = 10

    def get_queryset(self):
        qs = Student.objects.all()
        return qs


@login_required(login_url= 'lecturer/login')
def updateAssignment(request, slug):
    assignment = Assignment.objects.get(slug = slug)
    form = addAssignmentForm(request.POST or None, request.FILES or None, instance = assignment)
    if form.is_valid():
        ass = form.cleaned_data.get('course_code')
        form.save()
        messages.success(request, f'Assignment for {ass} Updated Successfully!')
        return redirect('view_assignment')
    
    
    return render(request, 'lecturer/update_assignment.html', {'form':form})

@login_required(login_url= 'lecturer/login')
def addLecture(request):
    form = addLectureForm()
    if request.method == 'POST':
        form = addLectureForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.lecturer = request.user.lecturer
            lecture = form.cleaned_data.get('course_code')
            form.save()
            messages.success(request, 'Lecture for ' + lecture + ' added successfully!')
            return redirect('view_lectures')
    else:
       form = addLectureForm()
    
 
    return render(request, 'lecturer/add_lecture.html', context = {'form':form})

@login_required(login_url= 'lecturer/login')
def updateLecture(request, slug):
    lecture = Lecture.objects.get(slug=slug)
    update = addLectureForm(request.POST or None, request.FILES or None, instance = lecture)
    if update.is_valid():
        course = update.cleaned_data.get('course_code')
        update.save()
        messages.success(request, f'Lecture for {course} Updated Successfully!')
        return redirect('view_lectures')

    return render(request, 'lecturer/update_lecture.html', {'update':update})

   
class LectureListView(ListView):
    template_name = 'lecturer/view_lectures.html'
    context_object_name = 'lectures'
    ordering = ['-date_created']
    # paginate_by = 10

    def get_queryset(self):
        qs = Lecture.objects.all()
        return qs

class StudentLectureListView(ListView):
    template_name = 'student/view_lectures.html'
    context_object_name = 'lecture_list'
    ordering = ['-date_created']
    # paginate_by = 10

    def get_queryset(self):
        qs = Lecture.objects.filter(level=self.request.user.student.level)
        return qs


@login_required(login_url= 'lecturer/login')
def deleteAssignment(request, slug):
    assignment = Assignment.objects.get(slug = slug)
    if request.method == 'POST':
        assignment.delete()
        messages.info(request, 'Assignment Deleted Successfully!')
        return redirect('view_assignment')
        
    context = {
        'assignment': assignment
    }

    return render(request, 'lecturer/delete.html', context)

@login_required(login_url= 'login')
def studentProfile(request):
    if request.method == 'POST':
        u_form = userUpdateProfileForm(request.POST, instance = request.user)
        p_form = studentUpdateProfileForm(request.POST, request.FILES, instance = request.user.student)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Profile Updated Successfully!')
            return redirect('student_profile')
    else:
        u_form = userUpdateProfileForm(instance = request.user)
        p_form = studentUpdateProfileForm(instance = request.user.student) 

    context = {

        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'student/profile.html', context)

def faq(request):

    return render(request, 'student/faq.html', {})

def forum(request):

    return render(request, 'student/forum.html', {})