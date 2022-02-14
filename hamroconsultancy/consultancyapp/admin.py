from django.contrib import admin

# Register your models here.
from .models import StudyField, University, CollegeDetails, CourseDetails

admin.site.register(StudyField)
admin.site.register(University)
admin.site.register(CollegeDetails)
admin.site.register(CourseDetails)