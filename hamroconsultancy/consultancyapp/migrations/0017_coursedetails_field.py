# Generated by Django 4.0.3 on 2022-04-12 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultancyapp', '0016_studyfield_fielddescrib'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursedetails',
            name='field',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='consultancyapp.studyfield'),
        ),
    ]
