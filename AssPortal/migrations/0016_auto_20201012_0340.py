# Generated by Django 3.1.2 on 2020-10-12 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0015_auto_20201012_0203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assresponse',
            name='date_uploaded',
            field=models.DateField(auto_now_add=True, null=True, verbose_name='Date Uploaded'),
        ),
    ]