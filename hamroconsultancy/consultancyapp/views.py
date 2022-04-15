from django.shortcuts import render, redirect
from .models import StudyField, University, CollegeDetails, CourseDetails, QuestionModel, Admission, CollegeCourse
from .forms import CreateUserForm
from .filters import CollegeFilter, CourseFilter, UniFilter
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def search(request):

    search = request.POST.get("search")
    college = CollegeDetails.objects.filter(collegeName__contains=search)
    course = CourseDetails.objects.filter(courseTitle__contains=search)
        
    if(college):
        paginator = Paginator(college, 10) # Show 5 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'app/colleges.html', {'search': search, 'college':page_obj})
    if(course):
        paginator = Paginator(course, 10) # Show 5 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'app/courses.html', {'search': search, 'course':course})


# Create your views here.
def dashboard(request):
    fields = StudyField.objects.all()
    university = University.objects.all()
    colleges=CollegeDetails.objects.all()[:5]
    courses=CourseDetails.objects.all()
    collegecourse=CollegeCourse.objects.all()
    paginator = Paginator(courses, 10) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    if request.method == "POST":
        return search(request)
        
    context = {'fields':fields, 'university':university, 'colleges':colleges,'courses':courses, 'collegecourse':collegecourse}
    return render(request, 'app/home.html', context)

def courses(request):
    courses=CourseDetails.objects.all()
    uni =University.objects.all()
    myFilter=CourseFilter(request.GET, queryset=courses)
    courses=myFilter.qs
    paginator = Paginator(courses, 10) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    
    if request.method == "POST":
        return search(request)
        
    context={'courses':page_obj, 'uni':uni,'myFilter':myFilter}
    return render(request, 'app/courses.html', context)

def studyfield(request, pk):
    field=StudyField.objects.get(fieldName=pk)
    context={'field':field}
    return render(request, 'app/studyField.html', context)

def colleges(request):
    colleges=CollegeDetails.objects.all()
    uni =University.objects.all()
    myFilter=CollegeFilter(request.GET, queryset=colleges)
    # uniFilter =UniFilter(request.GET, queryset=colleges)
    colleges=myFilter.qs
    # colleges=uniFilter.qs
    if request.method == "POST":
        return search(request)

    paginator = Paginator(colleges, 10) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'colleges':page_obj,'uni':uni,'myFilter':myFilter}
    return render(request, 'app/colleges.html', context)

def admission(request):
    admi = Admission.objects.all()
    if request.method == "POST":
        return search(request)
    context = {'admi':admi}
    return render(request, 'app/admission.html', context)

def about(request):
    if request.method == "POST":
        return search(request)
    return render(request, 'app/about.html')

@login_required(login_url='login')
def news(request):
    return render(request, 'app/news.html')
    
def courseDetail(request, pk):
    courses=CourseDetails.objects.get(couId=pk)
    context={'courses':courses}
    return render(request, 'app/courseDetail.html', context)

def collegeDetail(request, pk):
    colleges=CollegeDetails.objects.get(collegeId=pk)
    
    context = {'colleges':colleges}
    return render(request, 'app/collegeDetail.html', context)

def university(request):
    universities = University.objects.all()
    myFilter=UniFilter(request.GET, queryset=universities)
    universities=myFilter.qs
    context = {'universities':universities, 'myFilter':myFilter}

    return render(request, 'app/universities.html', context)

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = form.save()
            messages.success(request, 'Account was created for' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'app/register.html', context)
    
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            redirect('home')
        else:
            messages.info(request, "Username or Password incorrect")

    context = {}
    return render(request, 'app/login.html', context)

def logoutuser(request):
    logout(request)
    return redirect('login')

def quiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuestionModel.objects.all()
        ans=""
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q)
        
            if q.op1 ==  request.POST.get(q.question):
                ans="BBA/BBM/BBS/BIT"
                correct+=1
            elif q.op2 == request.POST.get(q.question):
                ans="Engineering field/CsIT/BIT "
            elif q.op3 == request.POST.get(q.question):
                ans="Arts and Humanity/ BHM"
            elif q.op4 == request.POST.get(q.question):
                ans="Medical Studies"
            else:
                wrong+=1
        
        context = {
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'total':total,
            'ans':ans
        }
        return render(request,'app/quizresult.html',context)
    else:
        questions=QuestionModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'app/quiz.html',context)

def userProfile(request):
    return render(request,'app/profile.html')