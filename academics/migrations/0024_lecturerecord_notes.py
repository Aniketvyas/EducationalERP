# Generated by Django 3.0.5 on 2021-04-19 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academics', '0023_lecturerecord'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecturerecord',
            name='notes',
            field=models.FileField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]