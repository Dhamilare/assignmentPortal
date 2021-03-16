from django.contrib.auth.models import User
import re
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import (Student, Lecturer, 
TITLE_CHOICES, Assignment, Lecture,
 LEVEL_CHOICES, assResponse, Grade )
from django.contrib.auth import authenticate
from django import forms


class StudentRegForm(forms.ModelForm):
    
    class Meta:
     model = Student
     exclude = ['user']
    
    email = forms.EmailField(
        widget = forms.EmailInput(attrs = {'placeholder': 'Email', 'class': 'form-control'})
    )
    
    username = forms.CharField(
        max_length = 20,
        widget = forms.TextInput(attrs = {'placeholder': 'Username', 'class': 'form-control'})
    )
    
    first_name = forms.CharField(
        max_length = 20,
        widget = forms.TextInput(attrs = {'placeholder': 'First Name', 'class': 'form-control'})
    )
    
    last_name = forms.CharField(
        max_length = 20,
        widget = forms.TextInput(attrs = {'placeholder': 'Last Name', 'class': 'form-control'})
    )
    
    matric_no = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Matric No (12/69/0000)', 'class': 'form-control'})
        
    )

    level = forms.CharField(
        widget = forms.Select(choices = LEVEL_CHOICES, attrs = {'class': 'form-control'})
    )
    
    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs = {'placeholder': 'Password', 'class': 'form-control'}),
        min_length = 8
    )
    
    password2 = forms.CharField(
        widget = forms.PasswordInput(attrs = {'placeholder': 'Confirm Password', 'class': 'form-control'}),
        min_length = 8
    )     
    
    image = forms.ImageField(
        required = True,
        widget = forms.FileInput(attrs = {'class': 'form-control', 'required':'false'})
    )
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('Passwords Do not Match')
        
        
    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            User.objects.get(email = email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('Email Already Exist')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('The User Name already exits')

    def clean_matric_no(self):
        matric_no = self.cleaned_data['matric_no']
        try:
            Student.objects.get(matric_no = matric_no)
        except ObjectDoesNotExist:
            return matric_no
        raise forms.ValidationError('Matric No already exits')
    
        
        
class LecturerRegForm(forms.ModelForm):
    class Meta:
        model = Lecturer
        exclude = ['user']
        
    username = forms.CharField(
        max_length = 20,
        widget = forms.TextInput(attrs = {'placeholder': 'Username', 'class': 'form-control'})
    )
        
    email = forms.EmailField(
        widget = forms.EmailInput(attrs = {'placeholder': 'Email', 'class': 'form-control'})
        )
        
    TITLE_CHOICES
        
    first_name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'First Name', 'class': 'form-control'})
        )
        
    last_name = forms.CharField(
        widget = forms.TextInput(attrs = {'placeholder': 'Last Name', 'class': 'form-control'})
            
        )
        
    password1 = forms.CharField(
        widget = forms.PasswordInput(attrs = {'placeholder': 'Password', 'class': 'form-control'}),
        min_length = 8
        )
        
    password2 = forms.CharField(
        widget = forms.PasswordInput(attrs = {'placeholder': 'Confirm Password', 'class': 'form-control'}),
        min_length = 8
        )
    
    image = forms.ImageField(
        widget = forms.FileInput(attrs = {'class': 'form-control'})
    )
    
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
            raise forms.ValidationError('Passwords Do not Match')
        
        
    def clean_email(self):
        email=self.cleaned_data['email']
        try:
            User.objects.get(email = email)
        except ObjectDoesNotExist:
            return email
        raise forms.ValidationError('Email Already Exist')
    
    def clean_username(self):
        username = self.cleaned_data['username']
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('The User Name already exits')
    
class addAssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        # exclude = ['user']
        exclude = ['lecturer']
    # course_code = forms.CharField(
    #     widget = forms.TextInput(attrs = {'class': 'form-control'})
    #     )
        
    # topic = forms.CharField(
    #      max_length = 100,
    #     widget = forms.TextInput(attrs = {'class': 'form-control'})
    #     )
        
    # question = forms.CharField(
    #     widget = forms.Textarea(attrs = {'class': 'form-control'})
    #     )
        
    # material = forms.FileField(
    #     widget = forms.ClearableFileInput(attrs = {'class': 'form-control', 'multiple':True, 'required':False})     
    #     )
        
    # due_date = forms.DateTimeField(
    #     widget = forms.DateInput(format = ('%m/%d/%Y'), attrs = {'class': 'form-control', 'type': 'datetime-local'})
    #     )

    # level = forms.CharField(
    #     widget = forms.Select(choices = LEVEL_CHOICES, attrs = {'class': 'form-control'})
    #     )

    def __init__(self, *args, **kwargs):
        super(addAssignmentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class submitAssignmentForm(forms.ModelForm):
    class Meta:
        model = assResponse
        fields = ['response', 'uploaded_content']

    def __init__(self, *args, **kwargs):
        super(submitAssignmentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['mark', 'remarks']

    def __init__(self, *args, **kwargs):
        super(ResponseForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class addLectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        exclude = ['lecturer']

    def __init__(self, *args, **kwargs):
        super(addLectureForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    # def clean_course_code(self):
    #     course_code = self.cleaned_data['course_code']
    #     qs = course_code
    #     try:
    #         Lecture.objects.get(course_code = qs)
    #     except ObjectDoesNotExist:
    #         return qs
    #     raise forms.ValidationError(qs + ' Already Exist')

    # def clean_course_title(self):
    #     course_title = self.cleaned_data['course_title']
    #     qs = course_title
    #     try:
    #         Lecture.objects.get(course_title = qs)
    #     except ObjectDoesNotExist:
    #         return qs
    #     raise forms.ValidationError('The Course Title is Already Associated With Other Lecture')


class studentUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'email', 'image']

    def __init__(self, *args, **kwargs):
        super(studentUpdateProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class userUpdateProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username']

    def __init__(self, *args, **kwargs):
        super(userUpdateProfileForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
