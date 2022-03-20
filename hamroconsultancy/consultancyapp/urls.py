from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('courses/', views.courses, name="courses"),
    path('colleges/', views.colleges, name="colleges"),
    path('university/', views.university, name="university"),
    path('login/', views.login, name="login"),
    path('signin/', views.register, name="signin"),
    path('quiz/', views.quiz, name="quiz"),
    path('collegeDetail/', views.collegeDetail, name="collegeDetail"),
    path('courseDetail/', views.courseDetail, name="courseDetail"),
    path('admission/', views.admission, name="admission"),
    path('about/', views.about, name="about"),
    path('news/', views.news, name="news"),
]