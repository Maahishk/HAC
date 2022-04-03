# Generated by Django 4.0.3 on 2022-04-03 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultancyapp', '0013_alter_collegedetails_collegeid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('admisId', models.IntegerField(primary_key=True, serialize=False)),
                ('admissionTitle', models.CharField(max_length=1000)),
                ('admissionFrom', models.DateTimeField(auto_now_add=True)),
                ('admissionTill', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
