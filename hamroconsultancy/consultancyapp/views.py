from django.shortcuts import render
from .models import StudyField, University, CollegeDetails, CourseDetails, QuestionModel
from .forms import CreateUserForm

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
    context = {'universities':universities}

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
            print(q.ans)
            print()
            if q.ans ==  request.POST.get(q.question):
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
        return render(request,'app/result.html',context)
    else:
        questions=QuestionModel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'app/quiz.html',context)