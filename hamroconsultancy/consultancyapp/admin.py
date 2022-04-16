from django.contrib import admin

# Register your models here.
from .models import StudyField, University, CollegeDetails, CourseDetails, QuestionModel, Admission,CourseType,CollegeCourse, Scholarship, Career, Vacancies

admin.site.register(StudyField)
admin.site.register(University)
admin.site.register(CollegeDetails)
admin.site.register(CourseDetails)
admin.site.register(QuestionModel)
admin.site.register(Admission)
admin.site.register(CourseType)
admin.site.register(CollegeCourse)
admin.site.register(Vacancies)
admin.site.register(Scholarship)
admin.site.register(Career)