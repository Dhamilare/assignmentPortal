# Generated by Django 3.1.2 on 2020-11-02 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0055_grade_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='remarks',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]