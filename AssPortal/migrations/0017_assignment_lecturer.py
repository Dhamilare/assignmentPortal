# Generated by Django 3.1.2 on 2020-10-12 14:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0016_auto_20201012_0340'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='lecturer',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='AssPortal.lecturer'),
            preserve_default=False,
        ),
    ]
