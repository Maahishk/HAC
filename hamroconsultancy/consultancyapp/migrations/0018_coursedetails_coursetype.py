# Generated by Django 4.0.3 on 2022-04-12 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultancyapp', '0017_coursedetails_field'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetails',
            name='courseType',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
