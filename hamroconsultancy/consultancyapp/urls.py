from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='home'),
    path('courses/', views.courses, name="courses"),
    path('colleges/', views.colleges, name="colleges"),
    path('university/', views.university, name="university"),
    path('login/', views.loginPage, name="login"),
    path('signin/', views.register, name="signin"),
    path('quiz/', views.quiz, name="quiz"),
    path('collegeDetail/<str:pk>/', views.collegeDetail, name="collegeDetail"),
    path('courseDetail/<str:pk>/', views.courseDetail, name="courseDetail"),
    path('admission/', views.admission, name="admission"),
    path('about/', views.about, name="about"),
    path('news/', views.news, name="news"),
    path('logout/', views.logoutuser, name="logout"),
    path('profile/', views.userProfile, name="profile"),
    path('scholarships/', views.scholarship, name="scholarships"),
    path('career/', views.career, name="career"),
    path('vacancies/', views.vacancies, name="vacancies"),
    path('studyfield/<str:pk>/', views.studyfield, name="studyfield"),
]