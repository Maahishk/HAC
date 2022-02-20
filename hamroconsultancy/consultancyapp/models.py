from django.db import models

# Create your models here.
class  StudyField(models.Model):
    fieldName=models.CharField(max_length=100, null=True)
    simg=models.ImageField(
        upload_to="field_image",
        null=True, 
        blank=True)
    def __str__(self):
        return self.fieldName

class University(models.Model):
    uniId = models.IntegerField(primary_key=True)
    uniName= models.CharField(max_length=200)
    uniaddress = models.CharField(max_length=200)
    uniContact = models.CharField(max_length=13)
    logo = models.ImageField(upload_to="universities")
    
    def __str__(self):
        return self.uniName
class CollegeDetails(models.Model):
    collegeId= models.AutoField(primary_key=True)
    collegeImg = models.ImageField(upload_to="colleges")
    collegeName = models.CharField(max_length=200)
    collegeDescription = models.TextField(max_length=200, blank=True)
    collegeAddress = models.CharField(max_length=200, blank=True)
    collegecontact = models.CharField(max_length=200, blank=True)
    university = models.ForeignKey(University, null=True, blank=True,on_delete= models.SET_NULL)
    def __str__(self):
        return self.collegeName

class CourseDetails(models.Model):
    couId = models.AutoField(primary_key=True)
    courseTitle = models.CharField(max_length=200)
    courseDescription = models.TextField(max_length=200, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True)
    university = models.ForeignKey(University, null=True, on_delete=models.SET_NULL, blank=True)
    def __str__(self):
        return self.courseTitle
    
class CollegeCourse(models.Model):
    collegeId = models.ForeignKey(CollegeDetails(), null=True, blank=True, on_delete= models.SET_NULL)
    couId = models.ForeignKey(CourseDetails(), null=True, blank=True, on_delete= models.SET_NULL)

    def __str__(self):
        return self.couId+""+collegeId

class QuestionModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.question