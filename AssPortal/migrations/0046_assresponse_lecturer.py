# Generated by Django 3.1.2 on 2020-10-24 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AssPortal', '0045_remove_assresponse_lecturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='assresponse',
            name='lecturer',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='AssPortal.lecturer'),
            preserve_default=False,
        ),
    ]
