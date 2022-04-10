from django.shortcuts import render, redirect
from .models import StudyField, University, CollegeDetails, CourseDetails, QuestionModel, Admission
from .forms import CreateUserForm
from .filters import CollegeFilter, CourseFilter, UniFilter
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def dashboard(request):
    fields = StudyField.objects.all()
    university = University.objects.all()
    colleges=CollegeDetails.objects.all()[:5]
    courses=CourseDetails.objects.all()
    myFilter=CourseFilter(request.GET, queryset=courses)
    courses=myFilter.qs
    context = {'fields':fields, 'university':university, 'colleges':colleges,'courses':courses,'myFilter':myFilter}
    return render(request, 'app/home.html', context)

def courses(request):
    courses=CourseDetails.objects.all()
    uni =University.objects.all()
    
    paginator = Paginator(courses, 5) # Show 5 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    myFilter=CourseFilter(request.GET, queryset=courses)
    courses=myFilter.qs
    context={'courses':page_obj, 'uni':uni,'myFilter':myFilter}
    return render(request, 'app/courses.html', context)

def colleges(request):
    colleges=CollegeDetails.objects.all()
    uni =University.objects.all()
    myFilter=CollegeFilter(request.GET, queryset=colleges)
    # uniFilter =UniFilter(request.GET, queryset=colleges)
    
    colleges=myFilter.qs
    # colleges=uniFilter.qs

    paginator = Paginator(colleges, 5) # Show 5 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'colleges':page_obj,'uni':uni,'myFilter':myFilter}
    return render(request, 'app/colleges.html', context)

def admission(request):
    admi = Admission.objects.all()
    context = {'admi':admi}
    return render(request, 'app/admission.html', context)

def about(request):
    return render(request, 'app/about.html')

@login_required(login_url='login')
def news(request):
    return render(request, 'app/news.html')
    
def courseDetail(request):
    courses=CourseDetails.objects.all()
    context={'courses':courses}
    return render(request, 'app/courseDetail.html', context)

def collegeDetail(request):
    colleges=CollegeDetails.objects.all()
    
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
    
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, username)
            redirect('home')
        else:
            messages.info("Username or Password incorrect")

    context = {}
    return render(request, 'app/login.html', context)

def quiz(request):
    if request.method == 'POST':
        print(request.POST)
        questions=QuestionModel.objects.all()
        score=0
        wrong=0
        correct=0
        total=0
        for q in questions:
            total+=1
            print(request.POST.get(q.question))
            print(q)
        
            if q.op1 ==  request.POST.get(q.question):
                score+=10
                correct+=1
            else:
                wrong+=1
        percent = score/(total*10) *100
        context = {
            'score':score,
            'time': request.POST.get('timer'),
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
        }
        return render(request,'app/quizresult.html',context)
    else:
        questions=QuestionModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'app/quiz.html',context)