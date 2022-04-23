import django_filters 

from .models import *

class CollegeFilter(django_filters.FilterSet):
    class Meta:
        model = CollegeDetails
        fields=['university']

class CourseFilter(django_filters.FilterSet):
    class Meta:
        model = CourseDetails
        fields=['university', 'courseType']

class UniFilter(django_filters.FilterSet):
    class Meta:
        model = University
        fields=['uniName']       