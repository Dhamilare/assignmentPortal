# Generated by Django 3.1.2 on 2020-11-09 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0067_auto_20201109_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='AssPortal.student'),
        ),
    ]
