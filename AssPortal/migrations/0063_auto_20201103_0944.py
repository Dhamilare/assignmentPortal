# Generated by Django 3.1.2 on 2020-11-03 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0062_auto_20201103_0754'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='slug_course_code',
        ),
        migrations.RemoveField(
            model_name='assresponse',
            name='slug_course_code',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='slug_course_code',
        ),
    ]
