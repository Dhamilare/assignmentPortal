# Generated by Django 3.1.2 on 2020-11-02 16:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0058_auto_20201102_1630'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grade',
            old_name='question',
            new_name='response',
        ),
    ]
