# Generated by Django 3.1.2 on 2020-10-31 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0049_lecture_semester'),
    ]

    operations = [
        migrations.AddField(
            model_name='assresponse',
            name='is_accessed',
            field=models.BooleanField(default=False),
        ),
    ]
