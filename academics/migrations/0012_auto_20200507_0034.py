# Generated by Django 3.0.5 on 2020-05-06 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0011_auto_20200506_1949'),
    ]

    operations = [
        migrations.AddField(
            model_name='lectures',
            name='attendies',
            field=models.ManyToManyField(to='academics.stud_details'),
        ),
        migrations.DeleteModel(
            name='LectureEnrollment',
        ),
    ]
