# Generated by Django 3.1.2 on 2020-10-12 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0014_auto_20201012_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assresponse',
            name='question',
        ),
        migrations.AddField(
            model_name='assresponse',
            name='response',
            field=models.TextField(default='Good Job'),
            preserve_default=False,
        ),
    ]