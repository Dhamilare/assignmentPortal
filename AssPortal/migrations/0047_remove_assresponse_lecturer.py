# Generated by Django 3.1.2 on 2020-10-24 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0046_assresponse_lecturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assresponse',
            name='lecturer',
        ),
    ]
