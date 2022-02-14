from django.shortcuts import render
from .models import StudyField, University, CollegeDetails, CourseDetails

# Create your views here.
def dashboard(request):
    fields = StudyField.objects.all()
    university = University.objects.all()
    colleges=CollegeDetails.objects.all()
    courses=CourseDetails.objects.all()
    context = {'fields':fields, 'university':university, 'colleges':colleges,'courses':courses}
    return render(request, 'app/home.html', context)

def courses(request):
    courses=CourseDetails.objects.all()
    context={'courses':courses}
    return render(request, 'app/courses.html', context)

def colleges(request):
    colleges=CollegeDetails.objects.all()
    context = {'colleges':colleges}
    return render(request, 'app/colleges.html', context)

def university(request):
    universities = University.objects.all()
    context = {'universities':universities}

    return render(request, 'app/universities.html', context)
