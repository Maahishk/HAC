import django_filters 

from .models import *

class CollegeFilter(django_filters.FilterSet):
    class Meta:
        model = CollegeDetails
        fields=['collegeName']

class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = CourseDetails
        fields=['courseTitle']

class UniFilter(django_filters.FilterSet):
    class Meta:
        model = CollegeDetails
        fields=['university']       