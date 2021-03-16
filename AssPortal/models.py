from django.db import models
from random import randint, choice
from string import ascii_uppercase
from django.utils import timezone
import uuid
from django.contrib.auth.models import User
from django.shortcuts import reverse
from PIL import Image
from django.utils.text import slugify
from django.core.validators import MinValueValidator, MaxValueValidator
#from django.contrib.auth.models import AbstractUser

# Create your models here.

# def assID():
#     letters = ascii_uppercase
#     pin = "".join([str(randint(0,9)) for p in range(0,8)])
#     pin = choice(letters)+ pin + choice(letters)
#     return pin

TITLE_CHOICES = (
    ('Mr','Mr'),
    ('Mrs','Mrs'),
    ('Miss','Miss')
)

LEVEL_CHOICES = (
    ('ND I','ND I'),
    ('ND II','ND II'),
    ('HND I','HND I'),
    ('HND II','HND II')
)

SEMESTER_CHOICES = (

    ('FIRST SEMESTER', 'FIRST SEMESTER'),
    ('SECOND SEMESTER', 'SECOND SEMESTER')
)



class Student(models.Model):
        user = models.OneToOneField(User, on_delete = models.CASCADE)
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        matric_no = models.CharField(max_length=20, unique= True)
        email = models.EmailField()
        level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
        image = models.ImageField(upload_to = 'student/dp', blank = True, null = True)
        date_joined = models.DateTimeField(auto_now_add = True, null = True)
        is_student = models.BooleanField(default=False)
        
        class Meta:
           verbose_name = 'Student'
           verbose_name_plural = 'Students'

        
        def save(self, *args, **kwargs):
            if self.is_student != True:
                self.is_student = True
            return super(Student, self).save(*args, **kwargs)
        
        def __str__(self):
            return self.first_name + ' - ' +  self.matric_no

        def save(self):
            super().save()
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        
    
       
class Lecturer(models.Model):
        user = models.OneToOneField(User, on_delete = models.CASCADE)
        title = models.CharField(max_length= 4, choices = TITLE_CHOICES)
        first_name = models.CharField(max_length= 30)
        last_name = models.CharField(max_length= 30)
        email = models.EmailField()
        image = models.ImageField(upload_to = 'lecturer/dp', blank = True, null = True)
        date_joined = models.DateTimeField(auto_now_add = True, null = True)
        is_student = models.BooleanField(default=False)
        
        class Meta:
           verbose_name = 'Lecturer'
           verbose_name_plural = 'Lecturers'
           
        def __str__(self):
           return self.first_name + ' - ' + self.last_name

        def save(self):
            super().save()
            img = Image.open(self.image.path)

            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
        
    
    
class Lecture(models.Model):
        lecturer = models.ForeignKey(Lecturer, on_delete = models.CASCADE)
        slug = models.SlugField(null=True, blank=True)
        course_title = models.CharField(max_length= 50, null=True)
        course_code = models.CharField(max_length= 10, unique = True)
        course_unit = models.CharField(max_length= 4)
        handout = models.FileField(blank=True, null= True, help_text="Please upload material(s) for this course", upload_to = 'lecturer/Lectures')
        level = models.CharField(max_length = 20, verbose_name = 'Class', choices = LEVEL_CHOICES)
        date_created = models.DateField('Date Created', null= True, auto_now_add = True)
        semester = models.CharField(choices = SEMESTER_CHOICES, max_length = 30)

        def __str__(self):
            return self.course_code

        def save(self, *args, **kwargs):
            if self.slug is None and self.course_title:
                self.slug = slugify(f'{self.course_title}'-'{self.course_code}')
            return super(Lecture, self).save(*args, **kwargs)

        def get_download_link(self):
            return self.handout.url
        

class Assignment(models.Model):
        lecturer = models.ForeignKey('auth.User', on_delete= models.CASCADE)
        slug = models.SlugField(null=True,blank=True)
        level = models.CharField(max_length = 20, verbose_name = 'Class', choices = LEVEL_CHOICES)
        course_code = models.ForeignKey(Lecture, on_delete = models.CASCADE)
        topic = models.CharField(max_length= 100)
        question = models.TextField()
        due_date = models.DateField('Due Date', null= True)
        material = models.FileField(blank=True, null= True, help_text="Please upload material(s) for this assignment", upload_to = 'lecturer/Assignments')
        date_uploaded = models.DateField('Date Uploaded', null= True, auto_now_add = True)
        score = models.PositiveSmallIntegerField(validators = [MaxValueValidator(30)], default = 0)
        is_viewed = models.BooleanField(default=False)

        def __str__(self):
            return self.topic
        
        class Meta:
            ordering = ['-date_uploaded']

        def get_download_link(self):
            return self.material.url
        
        def save(self, *args, **kwargs):
            if self.slug is None and self.course_code:
                self.slug = slugify(str(self.course_code.course_code))
            return super(Assignment, self).save(*args, **kwargs)

        
    
class assResponse(models.Model):
    lecturer = models.CharField(max_length = 50)
    slug = models.SlugField(null=True,blank=True)
    question = models.CharField(max_length = 100)
    course_code = models.CharField(max_length = 10)
    response = models.TextField()
    matric_no = models.CharField(max_length = 20)
    uploaded_content = models.FileField(upload_to = 'student/Assignment_Response', blank = True, null = True)
    date_uploaded = models.DateField('Date Uploaded', null= True, auto_now_add = True)
    level = models.CharField(max_length = 20, verbose_name = 'Class')
    is_accessed = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-date_uploaded']
    
    def __str__(self):
        return self.course_code

    def get_absolute_url(self):
        return reverse('assignment_detail', kwargs={"pk": self.pk})

    def get_download_link(self):
        return self.uploaded_content.url

    def save(self, *args, **kwargs):
            if self.slug is None and self.course_code:
                self.slug = slugify(self.course_code)
            return super(assResponse, self).save(*args, **kwargs)

class Grade(models.Model):
    lecturer = models.ForeignKey(Lecturer, on_delete = models.CASCADE)
    mark = models.PositiveSmallIntegerField(validators = [MaxValueValidator(30)], default = 0)
    remarks = models.CharField(max_length = 100, blank = True, null = True)
    question = models.CharField(max_length = 100)
    response = models.CharField(max_length = 100)
    student = models.ForeignKey(Student, on_delete= models.CASCADE)
    course_code = models.CharField(max_length = 10)
    level = models.CharField(max_length = 20)

    def __str__(self):
        return str(self.student)

class Topic(models.Model):
    title = models.CharField(max_length = 100)
    creator = models.ForeignKey(Student, on_delete = models.SET_NULL, null = True)
    details = models.TextField()
    views = models.IntegerField(default = 0)
    date_created = models.DateField()
    time_created = models.TimeField()
    slug = models.SlugField(null = True, blank = True)

    def __str__(self):
        return self.creator

    def save(self, *args, **kwargs):
        if self.slug is None and self.title:
            self.slug = slugify(self.title)
        return super(Topic, self).save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(max_length = 100)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.name


class Reply(models.Model):
    user = models.ForeignKey(Student, on_delete = models.SET_NULL, null = True)
    reply = models.CharField(max_length = 100)
    topic = models.ForeignKey(Topic, on_delete = models.SET_NULL, null = True)
    date_created = models.DateTimeField()

    def __str__(self):
        return self.user

    

    

