from django.contrib import admin
from .models import *

admin.site.site_header = "Assignment Portal Admin Panel"
admin.site.site_title = "Assignment Portal Admin Arera"
admin.site.index_title = "Welcome to the Assignment Portal Admin Area"


# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'matric_no')
    ordering = ['-id']
    
class LecturerAdmin(admin.ModelAdmin):
    list_display = ('title', 'first_name', 'last_name')
    ordering = ['-id']

class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'level', 'course_code', 'mark', 'remarks')
    ordering = ['-id']
    
class LectureAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'course_title', 'level', 'course_unit', 'semester')
    ordering = ['-id']
    
     
class AssignmentResponseAdmin(admin.ModelAdmin):
    list_display = ('course_code', 'matric_no', 'date_uploaded', 'level')  
    readonly_fields = ('matric_no', 'course_code', 'level', 'response','question', 'lecturer', 'slug')
    fieldsets = (
        (None, {
            'fields': ('course_code', 'slug','question','matric_no', 'level', 'lecturer')
            }),
    ('Assignment Details', {
        'fields': ('response','uploaded_content', 'is_accessed')
    }),
    )
    
class AssignmentAdmin(admin.ModelAdmin):
   list_display = ('course_code', 'topic', 'question', 'date_uploaded','due_date', 'level', 'score')


class TopicAdmin(admin.ModelAdmin):
   list_display = ('title', 'creator')  
#     inlines = [AssignmentResponseInline]

class ReplyAdmin(admin.ModelAdmin):
   list_display = ('user', 'reply', 'topic')

class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name', 'date_created')  

admin.site.register(Student, StudentAdmin)
admin.site.register(Lecturer, LecturerAdmin)
admin.site.register(Assignment, AssignmentAdmin)
admin.site.register(Lecture, LectureAdmin)   
admin.site.register(assResponse, AssignmentResponseAdmin)
admin.site.register(Grade, GradeAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(Category, CategoryAdmin)
