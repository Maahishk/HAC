from django.contrib import admin

# Register your models here.
from .models import StudyField, University, CollegeDetails, CourseDetails, QuestionModel, Admission,CourseType,CollegeCourse

admin.site.register(StudyField)
admin.site.register(University)
admin.site.register(CollegeDetails)
admin.site.register(CourseDetails)
admin.site.register(QuestionModel)
admin.site.register(Admission)
admin.site.register(CourseType)
admin.site.register(CollegeCourse)