# Generated by Django 3.1.2 on 2020-10-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0002_auto_20201011_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='level',
            field=models.CharField(choices=[('ND I', 'ND I'), ('ND II', 'ND II'), ('HND I', 'HND I'), ('HND II', 'HND II')], max_length=20, verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='level',
            field=models.CharField(choices=[('ND I', 'ND I'), ('ND II', 'ND II'), ('HND I', 'HND I'), ('HND II', 'HND II')], max_length=20, verbose_name='Class'),
        ),
    ]
