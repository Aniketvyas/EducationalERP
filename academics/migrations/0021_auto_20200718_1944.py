# Generated by Django 3.0.5 on 2020-07-18 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0020_auto_20200718_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendence',
            name='attendanceFile',
            field=models.FileField(upload_to='attendance'),
        ),
    ]