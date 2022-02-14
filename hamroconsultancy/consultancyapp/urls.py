from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard),
    path('courses/', views.courses, name="courses"),
    path('colleges/', views.colleges, name="colleges"),
    path('university/', views.university, name="university"),
]