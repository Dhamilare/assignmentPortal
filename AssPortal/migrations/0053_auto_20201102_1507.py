# Generated by Django 3.1.2 on 2020-11-02 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0052_auto_20201102_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='score',
            field=models.PositiveIntegerField(max_length=30),
        ),
    ]
