from django.db import models

# Create your models here.
class  StudyField(models.Model):
    fieldName=models.CharField(max_length=100, null=True)
    fieldDescrib=models.CharField(max_length=20000000, null=True)
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
    collegeId= models.IntegerField(primary_key=True)
    collegeImg = models.ImageField(upload_to="colleges")
    collegeLogo=models.ImageField(upload_to="colleges", null=True, default="statics/images/album-default.png")
    collegeName = models.CharField(max_length=200)
    collegeDescription = models.TextField(max_length=10000000, blank=True)
    collegeAddress = models.CharField(max_length=200, blank=True)
    collegecontact = models.CharField(max_length=200, blank=True)
    collegerating = models.IntegerField(blank=True, default=0)
    website = models.CharField(max_length=200, blank=True, default="")
    university = models.ForeignKey(University, null=True, blank=True,on_delete= models.SET_NULL)
    def __str__(self):
        return self.collegeName

class CourseType(models.Model):
    typename=models.CharField(primary_key=True, max_length=50)

    def __str__(self):
        return self.typename

class CourseDetails(models.Model):
    couId = models.IntegerField(primary_key=True)
    field = models.ForeignKey(StudyField, null=True, blank=True,on_delete= models.SET_NULL)
    courseTitle = models.CharField(max_length=200)
    courseDescription = models.TextField(max_length=200, null=True, blank=True)
    duration = models.CharField(max_length=50, null=True)
    courseType = models.ForeignKey(CourseType, null=True, on_delete=models.SET_NULL)
    university = models.ForeignKey(University, null=True, on_delete=models.SET_NULL, blank=True)
    def __str__(self):
        return self.courseTitle
    
class CollegeCourse(models.Model):
    collegeId = models.ForeignKey(CollegeDetails(), null=True, blank=True, on_delete= models.SET_NULL)
    couId = models.ForeignKey(CourseDetails(), null=True, blank=True, on_delete= models.SET_NULL)

    def __int__(self):
        return self.parseString(collegeId)

class Admission(models.Model):
    admisId = models.IntegerField(primary_key=True)
    admissionTitle= models.CharField(max_length=1000)
    admissionFrom = models.CharField(max_length=200)
    admissionTill = models.CharField(max_length=200)
    def __str__(self):
        return self.admissionFrom

class QuestionModel(models.Model):
    question = models.CharField(max_length=200, null=True)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.question

class Scholarship(models.Model):
    s_Id = models.IntegerField(primary_key=True)
    s_Title= models.CharField(max_length=200)
    s_openFrom = models.CharField(max_length=100)
    s_until = models.CharField(max_length=100)
    s_img = models.ImageField(upload_to="scholar", null=True)
    status= models.CharField(max_length=100, null=True, blank=True)
    topic= models.CharField(max_length=200, null=True)
    requirement= models.TextField(max_length=10000, null=True, blank=True)
    info = models.TextField(max_length=10000, null=True, blank=True)
    def __str__(self):
        return self.s_Title

class Vacancies(models.Model):
    v_Id = models.IntegerField(primary_key=True)
    v_Title= models.CharField(max_length=200)
    v_openFrom = models.CharField(max_length=100)
    v_until = models.CharField(max_length=100)
    v_img = models.ImageField(upload_to="scholar", null=True)
    v_status= models.CharField(max_length=100, null=True, blank=True)
    v_topic= models.CharField(max_length=200, null=True)
    v_requirement= models.TextField(max_length=10000, null=True, blank=True)
    v_info = models.TextField(max_length=10000, null=True, blank=True)
    def __str__(self):
        return self.v_Title

class Career(models.Model):
    c_Id = models.IntegerField(primary_key=True)
    c_Title= models.CharField(max_length=100)
    c_img = models.ImageField(upload_to="scholar", null=True)
    c_topic= models.CharField(max_length=200, null=True)
    c_requirement= models.TextField(max_length=10000, null=True, blank=True)
    c_info = models.TextField(max_length=10000, null=True, blank=True)
    def __str__(self):
        return self.c_Title


class News(models.Model):
    nid =models.IntegerField(primary_key=True)
    newstitle=models.TextField(max_length=500, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    desc=models.TextField(max_length=100000, blank=True)
    def __str__(self):
        return self.newstitle