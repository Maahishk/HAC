# Generated by Django 3.1.1 on 2022-02-14 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consultancyapp', '0003_auto_20220214_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetails',
            name='university',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='consultancyapp.university'),
        ),
    ]
