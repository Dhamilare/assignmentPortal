# Generated by Django 3.1.2 on 2020-10-11 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0012_auto_20201012_0047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assresponse',
            name='matric_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AssPortal.student'),
        ),
    ]
