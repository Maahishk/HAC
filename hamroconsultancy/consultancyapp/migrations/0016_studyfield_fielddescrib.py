# Generated by Django 4.0.3 on 2022-04-12 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consultancyapp', '0015_alter_admission_admissionfrom_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studyfield',
            name='fieldDescrib',
            field=models.CharField(max_length=20000000, null=True),
        ),
    ]
