# Generated by Django 3.0.4 on 2020-04-14 16:51

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attendence',
            fields=[
                ('AttendenceID', models.BigIntegerField(primary_key=True, serialize=False)),
                ('AttendenceFile', django.contrib.postgres.fields.jsonb.JSONField()),
                ('LastUpdatedOn', models.DateField()),
                ('CreatedOn', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('DepartmentID', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('DepartmentName', models.CharField(max_length=100)),
                ('HeadOfDepartment', models.EmailField(max_length=254)),
                ('SpecializedCourse', models.BooleanField()),
                ('StartDate', models.DateField()),
                ('School', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('FirstName', models.CharField(max_length=20)),
                ('LastName', models.CharField(max_length=20)),
                ('Dob', models.DateField()),
                ('Doj', models.DateField()),
                ('Etype', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('FacultyID', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('FacultyName', models.CharField(max_length=50)),
                ('Ftype', models.CharField(max_length=30)),
                ('FieldOfExpertise', models.CharField(max_length=50)),
                ('FieldOfInterest1', models.CharField(max_length=35)),
                ('FieldOfInterest2', models.CharField(max_length=35)),
                ('FieldOfInterese3', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='lectures',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('LectureID', models.CharField(max_length=10)),
                ('LectureName', models.CharField(max_length=50)),
                ('LessonPlan', models.FileField(upload_to='media')),
                ('Semester', models.IntegerField()),
                ('Credit', models.CharField(max_length=10)),
                ('LastTaughtBy', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='stud_details',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('EnrollmentNumber', models.CharField(max_length=10)),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('MiddleName', models.CharField(blank=True, max_length=100)),
                ('program', models.CharField(max_length=35)),
                ('Specialization', models.CharField(blank=True, max_length=35)),
                ('BatchYear', models.CharField(max_length=10)),
                ('CurrSem', models.IntegerField()),
                ('Residential', models.BooleanField()),
                ('AccomodationID', models.BigIntegerField()),
                ('UniversityEmailID', models.CharField(max_length=100)),
                ('PersonalEmailID', models.CharField(max_length=100)),
                ('Phone', models.BigIntegerField()),
                ('StreetAddress', models.CharField(max_length=100)),
                ('District', models.CharField(max_length=10)),
                ('State', models.CharField(max_length=20)),
                ('PinCode', models.IntegerField()),
                ('ProtectedClass', models.CharField(blank=True, max_length=3)),
                ('LastQualification', models.CharField(max_length=5)),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.Department')),
            ],
        ),
        migrations.CreateModel(
            name='TempLectures',
            fields=[
                ('TempLectureID', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('LectureTitle', models.CharField(max_length=500)),
                ('Credit', models.CharField(max_length=10)),
                ('TempLessonPlan', models.FileField(upload_to='media')),
                ('CreatedBy', models.EmailField(max_length=254)),
                ('Branch', models.CharField(max_length=10)),
                ('LectureStatus', models.CharField(max_length=15)),
                ('Changes', models.FileField(upload_to='media')),
                ('LastChangesMadeBy', models.CharField(max_length=30)),
                ('LastApprovedBy', models.CharField(max_length=30)),
                ('NextSendTo', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='StudentLectureEnrollment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EnrollmentValidity', models.IntegerField()),
                ('LectureID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.lectures')),
                ('StudentID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.stud_details')),
                ('TaughtBy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academics.faculty')),
            ],
        ),
    ]