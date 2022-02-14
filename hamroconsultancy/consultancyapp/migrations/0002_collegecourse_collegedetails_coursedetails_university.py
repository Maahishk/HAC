# Generated by Django 3.1.1 on 2022-02-14 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultancyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseDetails',
            fields=[
                ('couId', models.IntegerField(primary_key=True, serialize=False)),
                ('courseTitle', models.CharField(max_length=200)),
                ('courseDescription', models.TextField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='University',
            fields=[
                ('uniId', models.IntegerField(primary_key=True, serialize=False)),
                ('uniName', models.CharField(max_length=200)),
                ('uniaddress', models.CharField(max_length=200)),
                ('uniContact', models.CharField(max_length=13)),
                ('logo', models.ImageField(upload_to='universities')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeDetails',
            fields=[
                ('collegeId', models.IntegerField(primary_key=True, serialize=False)),
                ('collegeImg', models.ImageField(upload_to='colleges')),
                ('collegeName', models.CharField(max_length=200)),
                ('collegeDescription', models.TextField(blank=True, max_length=200)),
                ('university', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='consultancyapp.university')),
            ],
        ),
        migrations.CreateModel(
            name='CollegeCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('collegeId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='consultancyapp.collegedetails')),
                ('couId', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='consultancyapp.coursedetails')),
            ],
        ),
    ]
