# Generated by Django 3.1.2 on 2020-10-16 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0033_auto_20201016_0244'),
    ]

    operations = [
        migrations.AddField(
            model_name='assresponse',
            name='assignment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AssPortal.assignment'),
            preserve_default=False,
        ),
    ]
