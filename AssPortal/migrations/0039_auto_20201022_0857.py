# Generated by Django 3.1.2 on 2020-10-22 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0038_lecture_lecturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assresponse',
            name='uploaded_content',
            field=models.FileField(blank=True, null=True, upload_to='student/Assignment_Response'),
        ),
    ]
