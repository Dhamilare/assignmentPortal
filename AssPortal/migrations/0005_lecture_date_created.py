# Generated by Django 3.1.2 on 2020-10-11 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0004_assresponse_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='date_created',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date Created'),
        ),
    ]