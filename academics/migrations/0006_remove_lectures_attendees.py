# Generated by Django 3.0.4 on 2020-04-15 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0005_lectures_attendees'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lectures',
            name='attendees',
        ),
    ]
