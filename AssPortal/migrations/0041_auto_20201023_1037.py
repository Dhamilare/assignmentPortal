# Generated by Django 3.1.2 on 2020-10-23 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0040_assignment_is_viewed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assresponse',
            name='matric_no',
            field=models.CharField(max_length=20),
        ),
    ]