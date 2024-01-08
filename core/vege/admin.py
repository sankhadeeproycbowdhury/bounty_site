from django.contrib import admin
from .models import *

admin.site.register(Receipe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)

class SubjectMarksAdmin(admin.ModelAdmin):
    list_display = ['student' , 'subject' , 'marks']
    
admin.site.register(SubjectMarks , SubjectMarksAdmin)


class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student' , 'student_rank' , 'date_of_report_card_generation']
    
admin.site.register(ReportCard,ReportCardAdmin)



