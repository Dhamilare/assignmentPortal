# Generated by Django 3.1.2 on 2020-10-13 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0020_auto_20201013_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='lecturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AssPortal.lecturer'),
        ),
    ]